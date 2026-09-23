from unittest.mock import Mock
from uuid import uuid4

import pytest

import app
from db import add_item, get_connection, init_db, list_items


@pytest.fixture
def conn():
    connection = get_connection()
    schema_name = f"test_items_{uuid4().hex}"
    with connection.cursor() as cur:
        cur.execute(f'CREATE SCHEMA "{schema_name}"')
        cur.execute(f'SET search_path TO "{schema_name}"')
    connection.commit()
    try:
        init_db(connection)
        yield connection
    finally:
        with connection.cursor() as cur:
            cur.execute(f'DROP SCHEMA "{schema_name}" CASCADE')
        connection.commit()
        connection.close()


def test_list_items_starts_empty(conn):
    assert list_items(conn) == []


def test_add_item_returns_new_id(conn):
    item_id = add_item(conn, "wrench")
    assert item_id is not None


def test_list_items_returns_added_items(conn):
    add_item(conn, "wrench")
    add_item(conn, "hammer")

    items = list_items(conn)

    assert [name for _, name in items] == ["wrench", "hammer"]


def test_add_command_adds_item(monkeypatch):
    connection = Mock()
    add = Mock()
    monkeypatch.setattr(app, "get_connection", lambda: connection)
    monkeypatch.setattr(app, "init_db", Mock())
    monkeypatch.setattr(app, "add_item", add)

    assert app.main(["add", "wrench"]) is None

    add.assert_called_once_with(connection, "wrench")
    connection.close.assert_called_once()


def test_list_command_prints_items(monkeypatch, capsys):
    connection = Mock()
    monkeypatch.setattr(app, "get_connection", lambda: connection)
    monkeypatch.setattr(app, "init_db", Mock())
    monkeypatch.setattr(app, "list_items", lambda _: [(1, "wrench")])

    assert app.main(["list"]) is None

    assert capsys.readouterr().out == "1: wrench\n"


def test_help_command_does_not_connect_to_database(monkeypatch, capsys):
    monkeypatch.setattr(app, "get_connection", lambda: pytest.fail("unexpected database connection"))

    assert app.main(["help"]) is None

    assert capsys.readouterr().out == app.HELP_TEXT

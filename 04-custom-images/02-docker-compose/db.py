"""Minimal data access layer backed by the PostgreSQL sidecar container."""

import os

import psycopg2


def get_connection():
    """Open a connection using the docker-compose 'db' service defaults."""
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "localhost"),
        port=os.environ.get("POSTGRES_PORT", "5432"),
        dbname=os.environ.get("POSTGRES_DB", "postgres"),
        user=os.environ.get("POSTGRES_USER", "postgres"),
        password=os.environ.get("POSTGRES_PASSWORD", "postgres"),
    )


def init_db(conn):
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            )
            """
        )
    conn.commit()


def add_item(conn, name):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO items (name) VALUES (%s) RETURNING id", (name,))
        item_id = cur.fetchone()[0]
    conn.commit()
    return item_id


def list_items(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, name FROM items ORDER BY id")
        return cur.fetchall()


def clear_items(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM items")
    conn.commit()

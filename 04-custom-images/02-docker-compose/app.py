"""CLI entry point that stores and lists items in PostgreSQL."""

import sys

from db import add_item, get_connection, init_db, list_items


HELP_TEXT = """Usage:
  python app.py add <item>
  python app.py list
  python app.py help
"""


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv

    if args == ["help"]:
        print(HELP_TEXT, end="")
        return

    if not args:
        print(HELP_TEXT, end="")
        return

    command = args[0]
    if command == "add" and len(args) == 2:
        action = lambda conn: add_item(conn, args[1])
    elif command == "list" and len(args) == 1:
        action = lambda conn: None
    else:
        print(HELP_TEXT, end="", file=sys.stderr)
        return 1

    conn = get_connection()
    try:
        init_db(conn)
        action(conn)
        if command == "list":
            for item_id, name in list_items(conn):
                print(f"{item_id}: {name}")
    finally:
        conn.close()


if __name__ == "__main__":
    sys.exit(main() or 0)

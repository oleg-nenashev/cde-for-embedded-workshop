"""Minimal pytest suite for hello.py."""

from hello import GREETING, main


def test_main_prints_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert GREETING in captured.out

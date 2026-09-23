#!/usr/bin/env python3
"""Simple demo CLI for the Hello World dev container exercise."""

import platform
import sys

GREETING = "Hello, Embedded World!"


def main() -> None:
    print(GREETING)
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor() or 'unknown'}")


if __name__ == "__main__":
    main()

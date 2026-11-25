#!/usr/bin/env python3
"""Funniest one-line out-of-office reply.

Writes the reply to /output/entry.txt and prints exactly that one line.
Deterministic: same output on every run. Standard library only.
"""
import os

LINE = "I'm out of the office — my inbox is in charge now, and it's already asking for a raise."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

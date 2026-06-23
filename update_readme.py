#!/usr/bin/env python3
"""Pull the latest transmission and rewrite the profile README's live line."""
import re

SNAP = "feed.snapshot"
README = "README.md"


def latest():
    try:
        lines = [l.strip() for l in open(SNAP) if l.strip()]
    except FileNotFoundError:
        return None
    return lines[-1] if lines else None


def compact(line):
    parts = line.split()
    ts, callsign = parts[0], parts[1]
    hexes = [t for t in parts[3:] if re.fullmatch(r"[0-9A-F]{2}", t)]
    head = " ".join(hexes[:4])
    tail = " ".join(hexes[-3:])
    return ts, f"{callsign} ░ {head} ██ {tail}"


def build(ts, code):
    return (
        '<h1 align="center">⟁</h1>\n'
        '<p align="center"><em>builds at night. leaves before dawn.</em></p>\n\n'
        "<br>\n\n"
        f'<p align="center"><sub>last transmission · {ts}</sub></p>\n'
        f'<p align="center"><code>{code}</code></p>\n\n'
        "<br>\n\n"
        '<p align="center"><sub>the work speaks. i don\'t.</sub></p>\n'
        '<p align="center"><sub>♄</sub></p>\n'
    )


def main():
    line = latest()
    if not line:
        return
    ts, code = compact(line)
    open(README, "w").write(build(ts, code))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import even


def main():
    engine.start(even)


if __name__ == '__main__':
    main()

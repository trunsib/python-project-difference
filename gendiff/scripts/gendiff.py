#!/usr/bin/env python3
from gendiff.cli import parse_cli
from gendiff.generate_diff import generate_diff


def main():
    path1, path2, format = parse_cli()
    print(generate_diff(path1, path2, format))


if __name__ == '__main__':
    main()
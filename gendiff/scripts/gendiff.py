#!/usr/bin/env python3
from gendiff.cli import parse_cli
from gendiff import generate_diff


def main():
    path_file1, path_file2, format_name = parse_cli()
    diff = generate_diff(path_file1, path_file2, format_name)
    print(diff)


if __name__ == '__main__':
    main()
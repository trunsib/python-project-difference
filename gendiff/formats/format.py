from gendiff.formats import stylish
from gendiff.formats import plain
from gendiff.formats import create_json


def format_diff(diff, format_name):
    if format_name == 'stylish':
        return stylish.create_stylish(diff)
    elif format_name == 'plain':
        return plain.create_plain(diff)
    elif format_name == 'json':
        return create_json.create_json(diff)
    else:
        raise ValueError('Unknown format')
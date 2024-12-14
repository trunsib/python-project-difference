from gendiff.data import get_data
from gendiff.diff import diff
from gendiff.formats.format import format_diff


def generate_diff(path_file1, path_file2, format_name='stylish'):
    d1 = get_data(path_file1)
    d2 = get_data(path_file2)
    l_diff = diff(d1, d2)
    return format_diff(l_diff, format_name)

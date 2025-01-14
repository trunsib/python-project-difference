from gendiff.diff import get_diff
from gendiff.data import get_data
from gendiff.formats import format


def generate_diff(path_file1, path_file2, format_name='stylish'):
    d1 = get_data(path_file1)
    d2 = get_data(path_file2)
    l_diff = get_diff(d1, d2)
    return format(l_diff, format_name)
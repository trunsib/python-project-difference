from gendiff.diff import get_diff
from gendiff.data import get_data
from gendiff.formats.formatter import formating


def generate_diff(path1, path2, format='stylish'):
    data1 = get_data(path1)
    data2 = get_data(path2)
    diffs = get_diff(data1, data2)
    return formating(diffs, format)

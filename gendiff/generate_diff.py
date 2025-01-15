from gendiff.diff import get_diff
from gendiff.data import get_data
from gendiff.formats.formatter import formating


def generate_diff(first_file, second_file, format='stylish'):
    data1 = get_data(first_file)
    data2 = get_data(second_file)
    diffs = get_diff(data1, data2)
    return formating(diffs, format)

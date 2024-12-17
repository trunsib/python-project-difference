from gendiff.diff import get_diff
from gendiff.data import get_data
from gendiff.formats.format import format_diff


def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = get_data(filepath1)
    data2 = get_data(filepath2)
    diff = get_diff(data1, data2)

    return format_diff(diff, format_name)

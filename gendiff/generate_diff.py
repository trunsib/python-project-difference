from gendiff.diff import get_diff
from gendiff.data import get_data
from gendiff.formats.formatter import formating


def generate_diff(first_file_path, second_file_path, format_name='stylish'):
    data1 = get_data(first_file_path)
    data2 = get_data(second_file_path)
    diff = get_diff(data1, data2)

    return formating(diff, format_name)
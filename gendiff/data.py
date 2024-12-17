import json
import yaml
import os.path as path


def get_data(filepath1):
    with open(filepath1, 'r') as file:
        data = file.read()
        extension = path.splitext(filepath1)[1]
    return parse(data, extension)


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    elif extension == 'yml' or 'yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError('Unknown extension')

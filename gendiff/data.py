import os
import json
import yaml
from pathlib import Path
import os.path as path


def get_data(path_file):
    file_ext = Path(path_file).suffix
    path_file = Path() / 'tests/fixtures' / os.path.basename(path_file)
    with open(path_file) as f:
        s = f.read()
    return parse(s, file_ext)


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    elif extension == 'yml' or 'yaml':
        return yaml.safe_load(data)
    else:
        raise ValueError('Unknown extension')
    
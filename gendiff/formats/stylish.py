def create_stylish(d_list, lvl=0):
    res = []
    res.append('{\n')
    indent = ' ' * 2
    indent = indent + indent * 2 * lvl
    for node in d_list:
        op = ' '
        match node['status']:
            case 'nested':
                data = create_stylish(node['children'], lvl + 1)
            case 'added':
                data = сonvert_to_string(node['data'], indent)
                op = '+'
            case 'deleted':
                data = сonvert_to_string(node['data'], indent)
                op = '-'
            case 'changed':
                data = сonvert_to_string(node['data before'], indent)
                res.append(f"{indent}- {node['name']}: {data}\n")
                data = сonvert_to_string(node['data after'], indent)
                op = '+'
            case 'not changed':
                data = сonvert_to_string(node['data'], indent)
            case _:
                raise ValueError('Invalid type!')
        res.append(f"{indent}{op} {node['name']}: {data}\n")
    res.append(indent[:-2] + '}')
    return ''.join(res)


def сonvert_to_string(data, indent):
    if type(data) is dict:
        ind = indent + '    '
        res = '{\n'
        for key in data.keys():
            value = сonvert_to_string(data[key], indent)
            res = res + ind + '  ' + key + ': ' + value + '\n'
        res = res + indent[:-2] + '}'
    elif data is False or data is True:
        res = str(data).lower()
    elif data is None:
        res = 'null'
    else:
        res = str(data)
    return res

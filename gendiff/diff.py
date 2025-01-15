def get_diff(data1, data2):
    res = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        node = {'name': key}
        if key not in data1:
            node['status'] = 'added'
            node['data'] = data2[key]
        elif key not in data2:
            node['status'] = 'deleted'
            node['data'] = data1[key]
        elif type(data1[key]) is dict and type(data2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = get_diff(data1[key], data2[key])
        elif data1[key] == data2[key]:
            node['status'] = 'not changed'
            node['data'] = data1[key]
        else:
            node['status'] = 'changed'
            node['data before'] = data1[key]
            node['data after'] = data2[key]
        res.append(node)
    return res
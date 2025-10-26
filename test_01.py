data = [
    {"name": "Alice", "status": "ok", "response_time": 120},
    {"name": "Bob", "status": "fail", "response_time": 250},
    {"name": "Alice", "status": "ok", "response_time": 130},
    {"name": "Alice", "status": "fail", "response_time": 500},
    {"name": "Bob", "status": "ok", "response_time": 230}
]

# {
#   'Alice': {'ok': 2, 'fail': 1, 'avg_ok_time': 125.0},
#   'Bob':   {'ok': 1, 'fail': 1, 'avg_ok_time': 230.0}
# }


def test_statistic_counter():
    result = {}
    for el in data:
        if el['name'] not in result:
            if el['status'] == 'ok':
                result[el['name']] = {'ok':1, 'fail':0, 'avg_ok_time': el['response_time']}
            else:
                result[el['name']] = {'ok': 0, 'fail': 1, 'avg_ok_time': 0}
        else:
            if el['status'] == 'ok':
                result[el['name']]['ok'] += 1
                result[el['name']]['avg_ok_time'] += el['response_time']
                result[el['name']]['avg_ok_time'] = float(result[el['name']]['avg_ok_time'] / result[el['name']]['ok'])
            else:
                result[el['name']]['fail'] += 1
    return result
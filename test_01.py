def test_check_all_brackets() -> bool:
    s = "{[()]}"
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())  # {'(', '[', '{'}
    stack = []

    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in pairs:  # закрывающая скобка
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0


# users = [
#     {"id": 1, "name": "Иван", "age": 25},
#     {"id": 2, "name": "Анна", "age": -5},
#     {"id": 3, "name": "Петр", "age": 0},
#     {"id": 4, "name": "Сергей", "age": 31},
#     {"id": 5, "name": "", "age": 20}
# ]


def validate_users(users:list[dict])->list[dict]:
    valid = []
    for u in users:
        if u['name'] == '':
            continue
        if u['age'] < 1:
            continue
        valid.append(u)
    return valid


# orders1 = [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 50}]
# orders2 = [{'id': 2, 'amount': 70}, {'id': 3, 'amount': 40}]


def merge_order(ord_one, ord_two):
    result = {}
    result_arr = []
    for el in ord_one:
        result[el['id']] = el['amount']
    for el in ord_two:
        if el['id'] in result:
            result[el['id']] += el['amount']
        else:
            result[el['id']] = el['amount']
    for k, v in result.items():
        result_arr.append({'id': k, 'amount': v})
    return result_arr
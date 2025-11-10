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

# 31 10 2025

# orders = [
#     {"user": "Иван", "amount": 100},
#     {"user": "Иван", "amount": 200},
#     {"user": "Ольга", "amount": 0},
#     {"user": "Антон", "amount": 500},
#     {"user": "Антон", "amount": 500},
# ]


def test_rich_user():
    result = {}
    result_dict = []
    for el in orders:
        if el['user'] in result:
            result[el['user']] += el['amount']
        else:
            result[el['user']] = el['amount']

    for k, v in result.items():
        if v > 300:
            result_dict.append({"user": k, "total": v})

    return sorted(result_dict, key=lambda x: x['total'], reverse=True)


# 02 11 2025

# orders = [
#     {"id": 1, "amount": 100, "status": "paid"},
#     {"id": 2, "amount": 0, "status": "error"},
#     {"id": 3, "amount": 800, "status": "paid"},
#     {"id": 4, "amount": -50, "status": "paid"},
#     {"id": 5, "amount": 200, "status": "pending"},
#     {"id": 6, "amount": 0, "status": "paid"},
# ]

# [
#     {"id": 1, "amount": 100, "status": "paid", "tag": "small"},
#     {"id": 3, "amount": 800, "status": "paid", "tag": "big"},
# ]




def validate_and_tag(orders:list[dict]) -> list[dict]:
    result = []
    for order in orders:
        if order['status'] != 'paid' or order['amount'] <= 0:
            continue
        else:
            if order['amount'] < 300:
                status = 'small'
            elif order['amount'] < 700:
                status = 'medium'
            else:
                status = 'big'
            result.append({**order, "tag": status})
    return result

# def validate_and_tag(orders):
#     return [
#         {**o, "tag": "small" if o["amount"] < 300 else "medium" if o["amount"] < 700 else "big"}
#         for o in orders
#         if o["status"] == "paid" and o["amount"] > 0
#     ]

#

# 03 11 2025


# orders = [
#     {"id": 1, "amount": 120, "status": "paid"},
#     {"id": 2, "amount": -20, "status": "paid"},
#     {"id": 3, "amount": 900, "status": "paid"},
#     {"id": 4, "amount": 0, "status": "pending"},
#     {"id": 5, "amount": 450, "status": "paid"}
# ]
#
# # {"id": <id>, "tag": <"small" / "medium" / "big">}
#
# def list_comprehension(orders):
#     return[ {"id": el['id'], 'tag': 'small' if el['amount'] < 300 else 'medium' if el['amount'] < 700 else 'big'}
#             for el in orders if el['amount'] > 0 and el['status'] == 'paid' ]



# orders = [
#     {"id": 1, "items": [ {"name": "tea", "price": 200}, {"name": "cake", "price": 150} ]},
#     {"id": 2, "items": [ {"name": "coffee", "price": 0}, {"name": "sandwich", "price": 250} ]},
#     {"id": 3, "items": [ {"name": "juice", "price": 0}, {"name": "water", "price": 0} ]},
# ]
#
#
# # [
# #     {"id": 1, "status": "valid"},
# #     {"id": 2, "status": "has_free_item"},
# #     {"id": 3, "status": "invalid"}
# # ]
#
#
# def analyze_orders(orders):
#     return [{'id': el['id'], 'status': 'has_free_item' if any(item['price'] == 0 for item in el['items'])
#     else 'invalid' if all(item['price'] <= 0 for item in el['items']) else 'valid'} for el in orders]


#
# orders = [
#     {
#         "id": 1,
#         "items": [
#             {"name": "tea", "price": 200, "category": "drink"},
#             {"name": "cake", "price": 300, "category": "food"},
#         ],
#     },
#     {
#         "id": 2,
#         "items": [
#             {"name": "coffee", "price": 0, "category": "drink"},
#             {"name": "sandwich", "price": 400, "category": "food"},
#         ],
#     },
#     {
#         "id": 3,
#         "items": [
#             {"name": "water", "price": 0, "category": "drink"},
#             {"name": "cookie", "price": 0, "category": "food"},
#         ],
#     },
# ]
#
# # [
# #     {"id": 1, "food_items": 1, "drink_items": 1, "free_items": 0},
# #     {"id": 2, "food_items": 1, "drink_items": 1, "free_items": 1},
# #     {"id": 3, "food_items": 1, "drink_items": 1, "free_items": 2},
# # ]
#
#
# def summarize_orders(orders):
#     return [{'id': order['id'],
#              'food_items': sum(1 for item in order['items'] if item['category'] == 'food'),
#              'drink_items': sum (1 for item in order['items'] if item['category'] == 'drink'),
#              'free_items': sum(1 for item in order['items'] if item['price'] == 0)}
#             for order in orders]

#      BOOOOOOOM!



users = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
    {"id": 2, "name": "", "age": 0, "email": "bobexample.com"},
    {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@mail.com"},
    {"id": 4, "name": "Daisy", "age": 19, "email": "daisy@@mail.com"},
]


# "Alice (25) — alice@example.com"
# "Charlie (35) — charlie@mail.com"


def last_for_today(users):
    return [f"{el['name']} ({el['age']}) - {el['email']}"
            for el in users if el['name'] != '' and el['age'] > 0 and el['email'].count('@') == 1 ]


# 05 11 2025


orders = {
    "Alice": 1200,
    "Bob": 0,
    "Charlie": 450,
    "Daisy": 800,
    "Eve": 0,
}

# исключены пользователи с суммой <= 0
# имена ключей переведены в верхний регистр
# отсортировано по сумме (по убыванию)


def process_orders(data: dict) -> dict:
    sorted_dict = {k.upper() : v for k, v in data.items() if v > 0}
    return dict(sorted(sorted_dict.items(), key= lambda x: x[1], reverse=True))


def test_ord():
    print(process_orders(orders))



students = [
    {'name': 'Иван', 'score': 75},
    {'name': 'Мария', 'score': 92},
    {'name': 'Петр', 'score': 45},
    {'name': 'Ольга', 'score': 99},
    {'name': 'Сергей', 'score': 61}
]


# Отфильтровать только тех, у кого score >= 70
# Отсортировать их по убыванию score
# Вернуть список имён этих студентов в порядке убывания баллов


def top_students(data: list[dict]) -> list:
    top_list = [el for el in data if el['score'] > 69]
    sorted_top_list = sorted(top_list, key=lambda x: x['score'], reverse=True)
    return [el['name'] for el in sorted_top_list]


orders_05_11 = [
    {"id": 1, "user": "Alice", "amount": 120},
    {"id": 2, "user": "Bob", "amount": 0},
    {"id": 3, "user": "Charlie", "amount": 450},
    {"id": 4, "user": "Alice", "amount": 300},
    {"id": 5, "user": "Bob", "amount": 700}
]

# вернёт список имён пользователей,
# у которых суммарный amount > 500,
# отсортированный по убыванию суммы.


def best_costumers(orders:list[dict])-> list[str]:
    total = {}
    filtered = {}
    for o in orders:
        total[o['user']] = total.get(o['user'], 0) + o['amount']

    for k,v in total.items():
        if v > 500:
            filtered[k] = v
    return list(name for name, _ in sorted(filtered.items(), key= lambda x: x[1], reverse=True))



# 06 11 2025
# '{[[][][]}}('

def check_symbols(data)-> bool:
    pairs = {')':'(', '}':'{', ']':'['}
    stack = []

    for el in data:
        if el in pairs.values():
            stack.append(el)
        elif el in pairs:
            if not stack or pairs[el] != stack[-1]:
                return False
            stack.pop()
        else:
            return False

    return not stack

# fibonacci by python

def fibo(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
        return a


# 09 11 2025

# text = "Hello, hello world! World hello."
# {'hello': 3, 'world': 2}
import re

def words_counter(text):
    words_arr = re.split(r'[,?!. ]+', text)
    result = {}
    for word in words_arr:
        if word:
            word=word.lower()
            result[word] = result.get(word, 0) + 1
    return result

import re


text = "apple banana apple orange banana banana kiwi apple"
# [('apple', 3), ('banana', 3), ('kiwi', 1)]

def most_popular_words(words, positions):
    word_list = words.split(' ')
    counter = {}
    for w in word_list:
        counter[w] = counter.get(w, 0) + 1
    return list((word, value) for word, value in sorted(counter.items(), key= lambda x: (x[-1], x[0])))[:positions]
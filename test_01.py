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


# 12 11 2025

# players = [
#     {"name": "Petr", "wins": 5, "losses": 3},
#     {"name": "Anna", "wins": 5, "losses": 1},
#     {"name": "Ivan", "wins": 5, "losses": 1},
#     {"name": "Olga", "wins": 3, "losses": 4},
# ]
# --->
# [
#     {"name": "Anna", "wins": 5, "losses": 1},
#     {"name": "Ivan", "wins": 5, "losses": 1},
#     {"name": "Petr", "wins": 5, "losses": 3},
#     {"name": "Olga", "wins": 3, "losses": 4},
# ]


def top_players(players:list[dict]) -> list[dict]:
    return sorted(players, key=lambda x: (-x['wins'], x['losses', x['name']]))

def test_sobes():
    print(['123','da'][False][1]) # 2





import time

class A:
    def __init__(self):
        # Вызывается при создании объекта
        self.text = "IIM"

    @staticmethod
    # статический метод не требует экземпляра
    def what_time():
        return f"{time.time()}"

    @property
    # превращает метод в атрибут только для чтения.
    def useless_getter(self):
        return self.text

    def __private_or_public(self):
        # Имя искажается чз name-mangling. псевдо приватность
        return 1

    def __str__(self):
        # Магические методы обычно вызываются встроенными функциями: str(obj) вызывает str().
        return self.text


ob = A()

A.what_time()
ob.what_time()

ob.useless_getter

ob._A__private_or_public()

ob.__str__()


# just test

example_data = {
    "id":12,
    "discountPercentage": 0,
    "title": "boom",
    "price": 123
}

# import requests
#
# def test_base_check():
#     url = 'https://dummyjson.com/products'
#     response = requests.get(url)
#
#
#     assert response.status_code == 200
#     assert response.headers['content-type'].startswith('application/json')
#
#     data = response.json()
#     products = data['products']
#
#     assert 'products' in data
#     assert isinstance(products, list)
#
#     has_discount = False
#
#     for p in products:
#         assert isinstance(p, dict)
#         assert isinstance(p['title'], str)
#         assert p['id'] > 0
#         assert p['price'] > 0
#         assert 'discountPercentage' in p
#         if p['discountPercentage'] > 0:
#             has_discount = True
#     assert has_discount == True








import requests


BASE_URL = 'https://dummyjson.com/products'



def test_get_products_base():
    res = requests.get(f'{BASE_URL}?limit=5')
    data = res.json()

    assert res.status_code == 200
    assert res.headers['content-type'].startswith('application/json')
    assert 'products' in data

    products = data['products']

    assert isinstance(products, list)
    assert len(products) > 0

    for el in products:
        assert 'id' in el
        assert 'title' in el
        assert 'price' in el
        assert el['price'] > 0


def test_create_product():
    payload = {"title": "TestProduct", "price": 123}
    res = requests.post(f'{BASE_URL}/add', data=payload)
    data = res.json()

    assert res.status_code == 201
    assert 'id' in data
    assert 'title' in data
    assert 'price' in data
    assert isinstance(data['id'], int)
    assert data['title'] == payload['title']
    assert data['price'] == str(payload['price'])


def test_create_product_negative():
    payload = {'price':-12}
    res = requests.post(f'{BASE_URL}/add',payload)
    data = res.json()

    assert res.status_code == 400
    assert data['message'] == 'price must be more then zero'
#реально от сервера я получаю 201 created

import pytest

# а как обратиться к БД??
# а как проверять по схеме например validate / pydantic


# POST /auth/login

# Ответы:
# 200 — успех: {"token": "..."}
# 400 — пустые поля или неправильный тип данных
# 403 — неверные учетные данные


# Позитивный тест — успешная авторизация.
# Негативные тесты — параметризованные:
# пустой логин
# пустой пароль
# пустой логин и пароль
# неверный пароль
# неверный логин


class ApiClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def post(self, path, data=None, headers=None):
        return requests.post(f"{self.base_url}{path}", json=data, headers=headers)

    def get(self, path, params=None, headers=None):
        return  requests.get(f"{self.base_url}{path}",params=params, headers=headers)



@pytest.fixture
def api():
    return ApiClient(base_url = 'https://apolinapolis.ru')

@pytest.fixture
def auth_token(api):
    resp = api.post(path='/auth', data={"username": "zorro", "password": "123"})
    return resp.json()['token']

@pytest.fixture
def authorized_api(api, auth_token):
    api.headers['authorization'] = f'Bearer {auth_token}'
    return api



def test_authorization_valid(api):
    resp = api.post('auth/login', {'user':'roma', 'pass':'123'})
    data = resp.json()

    assert resp.status_code == 200
    assert 'token' in data
    assert isinstance(data['token'], str)

@pytest.mark.parametrize(
    "login, passw, code", [
        ('', '', 400),
        ('', '123', 400),
        ('roma', '', 400),
        ('roma', 'wrong', 403)
    ]
)
# def test_auth_negative(api, login, passw, code):
#     resp = api.post('auth/login', {'user': login, 'pass': passw})
#     assert resp.status_code == code


# 01.12.2025 decorators


def null_decorator(func):
    return 'decorated' + func

def upper_decorator(func):
    def wrapper():
        base_text = func()
        result = base_text.upper()
        return result
    return wrapper()

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper()



def greet():
    return 'Hello'



def test_01():
    print(upper_decorator(greet))


def double_list(arr):
    return [2* x for x in arr]

print(double_list([1, 2, 3]))

def count_chars(s:str):
    result = {}

    for elem in s:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result

print(count_chars("hello"))


def longest_word(arr:list[str]):
    result = ''
    for el in arr:
        if len(result) < len(el):
            result = el
    return result

print(longest_word(["python", "qa", "automation"]))



# 07 12 2025
def test_movie_zeros():
    data = [1,2,5,1,2,0,4,2,0,456,30,3]
    result = []
    zeros = []

    for el in data:
        if el == 0:
            zeros.append(el)
        else:
            result.append(el)
    result.extend(zeros)
    print(result)


def test_letters_mixer():
    example_data = "O tempora o mores !" # 'Oay emporatay oay oresmay !'
    result = example_data.split(' ')
    itog = ''
    for word in result:
        if word in ['!','?','.',',']:
            itog += word
        itog += word[1:]+word[0]+'ay '
    print(itog)


def total(*args):
    result = 0
    if args:
        for x in args:
            result += x
    return result

def merge_dict(**kwargs):
    return kwargs


def exception_try(x):
    try:
        return 100 / x
    except ZeroDivisionError:
        return 'ops!'
    finally:
        print('finally callback')

exception_try(0)



def file_reader(file):
    with open(file, 'r') as f:
        for i in range(3):
            line = f.readline()
            if not line:
                break
            print(line)






def self_read(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            result = []
            for _ in range(5):
                line = f.readline()
                if not line:
                    break
                result.append(line.strip('\r\n'))
            return result
    except FileNotFoundError:
        return 'file not found'


# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagram(words):
    result = {}
    for w in words:
        key = ''.join(sorted(w))
        if key in result:
            result[key].append(w)
        else:
            result[key] = [w]
    return result






# test merge
if __name__ == "__main__":
    print(sorted('sdgsdg'))
# Есть JSON, нужно вытащить из него уникальные цвета (color) для аксессуаров типа phoneCase:

json_data = {
    "phone": {
        "model": "CoolPhone",
        "screen": 5,
        "accessories": [
            {"type": "phoneCase", "color": "grey"},
            {"type": "phoneCase", "color": "blue"},
            {"type": "phoneCase", "color": "grey"},
            {"type": "phoneCase", "color": "blue"},
            {"type": "ScreenProtector", "color": "noColor"},
            {"type": "phoneCase", "color": "red"}
        ]
    }
}

uniq_colors = {acc['color'] for acc in json_data['phone']['accessories'] if acc['type'] == 'phoneCase'}

# найти наибольший int
s = 'i8sdgf928ury63jds9sf9a333'

def func(s):
    result = []
    current = ''

    for el in s:
        if el.isdigit():
            current += el
        else:
            if current:
                result.append(int(current))
                current = ''
    if current:
        result.append(int(current))
    return max(result)

print(func(s))

# TODO

# Страница https://company.local/api/v1/devices возвращает список устройств в JSON.
# Задача — получать ежеминутно список и записывать в CSV (device_name, interface_name).
# [{  "id": 1,
#     "name": "Device1",
#     "interfaces": [
#       {"id": 101, "name": "Ethernet0"},
#       {"id": 102, "name": "Ethernet1"}]}]
import csv
import time
import requests

URL = 'https://company.local/api/v1/devices'

def get_devices():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()


def parse_devices(devices_data):
    result = []
    for el in devices_data:
        dev_name = el.get('name')
        for interface in el.get('interfaces', []):
            interface_name = interface.get('name')
            result.append({'device_name':dev_name, 'interface_name':interface_name})
    return result


def save_to_csv(data):
    with open('devices.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['device_name','interface_name'])
        writer.writeheader()
        writer.writerows(data)


def devices_loop():
    while True:
        devices = get_devices()
        parsed_devices = parse_devices(devices)
        save_to_csv(parsed_devices)
        time.sleep(60)


# # Вернуть сумму вхождений
# statuses = 'skip, pass, failed, failed, pass, pass, error, skip, error, error'
#
def summarize_result(data:str)->dict:
    data = data.split(',')
    counter = {}
    for el in data:
        el = el.strip()
        if el in counter:
            counter[el]+=1
        else:
            counter[el] = 1
    return dict(sorted(counter.items(), key=lambda x: x[1], reverse=True)) # Добавлена сортировка
#
#
# # Вариант через импорт
# def summarize_result_two(data:str)->dict:
#     return dict(Counter(x.strip() for x in data.split(',')))


# Фикстуры и параметризация
# 1) Реализовать фикстуру, которая будет передавать список пользователей в тест.
# 2) Написать тест с фикстурой из 1: проверять, что среди пользователей нет несовершеннолетних.
# 2.1) Написать тест без фикстур, с параметризацией. Тест проверяет, что все пользователи не старше 60 лет.
# 3) Написать тест с фикстурой из 1: проверить, что есть пользователи из Москвы;
# вернуть их количество в фикстуру и вывести в консоль через print().

users_data = [{'name': 'Nikolay', 'last_name': 'Petrov', 'age': 43, 'city': 'Moscow'},
    {'name': 'Ivan', 'age': 43, 'last_name': 'Volkov', 'city': 'Rostov'},
    {'name': 'Sergey', 'age': 23, 'last_name': 'Pak', 'city': 'Yakutsk'},
    {'name': 'Ivan', 'age': 19, 'last_name': 'Ivanov', 'city': 'Tver'},
    {'name': 'Nikolay', 'age': 41, 'last_name': 'Ivanov', 'city': 'Moscow'}]

import pytest

@pytest.fixture
def users():
    return users_data

def test_no_less_18(users):
    for user in users:
        assert user['age'] >= 18

@pytest.mark.parametrize('user', users_data)
def test_less_60_users_age(user):
    assert user['age'] <= 60

@pytest.fixture
def msk_users_count(users):
    return len([u for u in users if u['city'] == 'Moscow'])

def test_moscow_users(msk_users_count):
    assert msk_users_count > 0
    print(f'it is {msk_users_count} users from Moscow')



# Чтобы fixture вызывалась в теле теста и возвращала список random int по длине count а после теста очищаем список
import random

def generate_item()->int:
    return random.randint(1,20)

@pytest.fixture
def setup_items():
    def _gen(count:int):
        return [generate_item() for _ in range(count)]
    return _gen

@pytest.fixture
def setup_items_clear():
    items = []
    def _gen(count:int):
        items.clear() #fix
        for _ in range(count):
            items.append(generate_item())
        return items
    yield _gen
    items.clear()

def op_test_a(setup_items):
    item_ids = setup_items(count=3)


# Уникальные символы = (
# O(n) / O(n2) methods
# from collections import Counter
#
# a = 'Su cc ess'
#
# def func_on(s: str) -> str:
#     s = s.lower()
#     counts = Counter(s)  # считаем все символы
#     result = []
#
#     for ch in s:
#         if counts[ch] == 1:
#             result.append('(')
#         else:
#             result.append(')')
#     return ''.join(result)
#
#
# def func_on2(string:str)->str:
#     data = string.lower()
#     result = []
#
#     for el in data:
#         if data.count(el)==1:
#             result.append('(')
#         else:
#             result.append(')')
#     return ''.join(result)


# # Вернуть сумму вхождений
# statuses = 'skip, pass, failed, failed, pass, pass, error, skip, error, error'
#
# def incoming_counter(str)->dict:
#     counter = {}
#     for el in str.split(','):
#         el = el.strip()
#         if el in counter:
#             counter[el] += 1
#         else:
#             counter[el] = 1
#     #return counter
#     return dict(sorted(counter.items(), key = lambda x: x[1], reverse=True))
#
# print(incoming_counter(statuses))


# Написать класс Car:  свойства color (текст),  price (нецелое число).
# Метод get_final_price — если цвет «красный», цена на 15% дороже от базовой.
# Создать класс HeavyCar, унаследованный от Car: свойство has_trailer (булево).
# Переопределить get_final_price: прицеп — +25% от базовой цены. Использовать super().
# Итог округлить до 2х цифр после запятой

class Car:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def get_final_price(self):
        if self.color == 'red':
            return self.price * 1.15
        return self.price


class HeavyCar(Car):
    def __init__(self, color, price, has_trailer):
        super().__init__(color, price)
        self.has_trailer = has_trailer

    def get_final_price(self, digits=2):
        final_price = super().get_final_price()
        if self.has_trailer:
            final_price += self.price * 0.25
        return round(final_price, digits)



# Что будет выведено? Если тест падает — как сделать, чтобы проходил?

class User:
    height = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name and self.age == other.age
        return NotImplemented

    def __hash__(self):
        return hash((self.name, self.age))
#
# def main():
#     user_set = set()
#     user_set.add(User("Max", 12))
#     user_set.add(User("Max", 12))
#     user_set.add(User("Max", 12))
#     user_set.add(User("Max", 12))
#     if len(user_set) == 1:
#         print("Passed!")
#     else:
#         print("Failed!")
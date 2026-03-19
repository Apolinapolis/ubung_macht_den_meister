# Вернуть сумму вхождений
statuses = 'skip, pass, failed, failed, pass, pass, error, skip, error, error'

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


# Вариант через импорт
def summarize_result_two(data:str)->dict:
    return dict(Counter(x.strip() for x in data.split(',')))


# Написать класс Car:  свойства color (текст),  price (нецелое число). Метод get_final_price — если цвет «красный», цена на 15% дороже от базовой.
# Создать класс HeavyCar, унаследованный от Car: свойство has_trailer (булево). Переопределить get_final_price: прицеп — +25% от базовой цены. Использовать super().

class Car:
    def __init__(self, color:str, price:float):
        self.color = color
        self.price = price

    def get_final_price(self):
        if self.color == 'red':
            return self.price * 1.15
        return self.price


class HeavyCar(Car):
    def __init__(self, color:str, price:float, has_trailer:bool):
        self.has_trailer = has_trailer
        super().__init__(color, price)

    def get_final_price(self, digits=2)->float:
        price = super().get_final_price()

        if self.has_trailer:
            price += self.price * 0.25

        return round(price, digits)


# Фикстуры и параметризация
# 1) Реализовать фикстуру, которая будет передавать список пользователей в тест.
# 2) Написать тест с фикстурой из 1: проверять, что среди пользователей нет несовершеннолетних.
# 2.1) Написать тест без фикстур, с параметризацией. Тест проверяет, что все пользователи не старше 60 лет.
# 3) Написать тест с фикстурой из 1: проверить, что есть пользователи из Москвы;
# вернуть их количество в фикстуру и вывести в консоль через print().

import pytest

@pytest.fixture
def users():
    return  [{'name': 'Nikolay', 'last_name': 'Petrov', 'age': 43, 'city': 'Moscow'},
    {'name': 'Ivan', 'age': 43, 'last_name': 'Volkov', 'city': 'Rostov'},
    {'name': 'Sergey', 'age': 23, 'last_name': 'Pak', 'city': 'Yakutsk'},
    {'name': 'Ivan', 'age': 19, 'last_name': 'Ivanov', 'city': 'Tver'},
    {'name': 'Nikolay', 'age': 41, 'last_name': 'Ivanov', 'city': 'Moscow'}]

def test_no_less_18(users):
    for user in users:
        assert user['age'] >= 18


users_data = [{'name': 'Nikolay', 'last_name': 'Petrov', 'age': 43, 'city': 'Moscow'},
    {'name': 'Ivan', 'age': 43, 'last_name': 'Volkov', 'city': 'Rostov'},
    {'name': 'Sergey', 'age': 23, 'last_name': 'Pak', 'city': 'Yakutsk'},
    {'name': 'Ivan', 'age': 19, 'last_name': 'Ivanov', 'city': 'Tver'},
    {'name': 'Nikolay', 'age': 41, 'last_name': 'Ivanov', 'city': 'Moscow'}]

@pytest.mark.parametrize('user', users_data)
def test_less_60_users_age(user):
    assert user['age'] <= 60

@pytest.fixture
def msk_users_count(users):
    return len([u for u in users if u['city'] == 'Moscow'])

def test_moscow_users(msk_users_count):
    assert msk_users_count > 0
    print(f'it is {msk_users_count} users from Moscow')


# Каков будет вывод?
def append_list(val, list=[]):
    list.append(val)
    return list

list_1 = append_list(10) # [10]
list_2 = append_list(123,[]) # [123]
list_3 = append_list('a') # [10,'a']

print(list_1, list_2, list_3)


# Каков будет вывод?
D={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print([i for i in range(3) if i in D.values()]) # [1,2]



# Каков будет вывод?
def func(val, *args, **kwargs):
    print(val)
    print(args)
    print(kwargs)

func("Hi", "Ozon", {"a": 1, "b": 2}, pi=3.14, e=2.71)


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



# Декоратор, который напишет start до и end после выполнения функции
def decor(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@decor
def summa(a,b=0):
    return print(a+b)

summa(1,10)

# Декоратор с отложенным запуском
import time


def decor_delay(sec):
    def decorator(func):
        def wrapper(*args,**kwargs):
            time.sleep(sec)
            return func(*args,**kwargs)
        return wrapper
    return decorator


@decor_delay(sec=10)
def summa(a,b=0):
    return print(a+b)


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
from collections import Counter

def func(s: str) -> str:
    counts = Counter(s)  # считаем все символы
    result = ''

    for ch in s:
        if not ch.isalpha():  # пропускаем пробелы/знаки
            continue
        if counts[ch] == 1:
            result += '('
        else:
            result += ')'
    print(counts)
    print(result)

a = 'fia asofdw as'
func(a)


# найти наибольший int

s = 'i8sdgf928ury63jds9sf9a3333'

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
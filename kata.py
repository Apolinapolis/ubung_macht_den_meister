from trace import Trace

from requests import session


class File:
    """CONTEXT"""
    def __init__(self,path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.path, self.mode)
        except FileNotFoundError:
            self.file = open(self.path, mode='w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.file:
            self.file.close()
        if exc_type and issubclass(exc_type, OSError):
            return True
        return False


with File('new.txt', mode='a') as f:
    print('creating file')



class Example:
    """Приватные методы"""
    def __init__(self):
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'

    @property
    def private(self):
        return self.__private

class Child(Example):
    'Dockstring only'


#IT_one задача на sql

# /*CREATE TABLE customers (
#  id INTEGER NOT NULL PRIMARY KEY,
#  name VARCHAR(30) NOT NULL,
#  cardNum INTEGER
# );*/
#
# CREATE TABLE accounts (
#  id INTEGER NOT NULL PRIMARY KEY,
#  customer_id INTEGER NOT NULL,
#  balance INTEGER,
#  payment_system VARCHAR(30) NOT NULL,
#  FOREIGN KEY (customer_id) REFERENCES customers(id)
# );
#
# INSERT INTO customers(id, name, cardNum) values(1, 'Иван Грозный', 4532);
# INSERT INTO customers(id, name, cardNum) values(2, 'Екатерина Романова', 7764);
# INSERT INTO customers(id, name, cardNum) values(3, 'Николай Романов', 2323);
# INSERT INTO customers(id, name, cardNum) values(4, 'Владимир Ленин', 9970);
# INSERT INTO customers(id, name, cardNum) values(5, 'Леонид Брежнев', 1231);
# INSERT INTO customers(id, name, cardNum) values(6, 'Борис Ельцин', NULL);
#
# INSERT INTO accounts(id, customer_id, balance, payment_system) values(1, 1, 123.00, 'VISA');
# INSERT INTO accounts(id, customer_id, balance, payment_system) values(2, 2, 555.00, 'VISA');
# INSERT INTO accounts(id, customer_id, balance, payment_system) values(3, 4, 222.00, 'MasterCard');
# INSERT INTO accounts(id, customer_id, balance, payment_system) values(4, 3, 333.00, 'MasterCard');
# INSERT INTO accounts(id, customer_id, balance, payment_system) values(5, 5, 444.00, 'UnionPay');
# INSERT INTO accounts(id, customer_id, balance, payment_system) values(6, 6, 0.00, 'UnionPay');
#
# 1. Вывести название и максимальный баланс для каждой платежной системы.
# 2. Вывести имя клиента, номер карты, баланс, платежную систему.
# 3. Только клиентов с платежной системой VISA, отсортировать по балансу по убыванию.


#Задачи на Python

# Описание:
# Требуется реализовать вывод функции print 2х классов: Parent, Child. При двух ограничениях:
# 1 - нельзя писать вывод Parent класса прямым текстом.
# 2 - нельзя менять наследуемость класса Child
# Можно менять поведение класса Child
# Результат вывести на экран.

# Входные данные:
# class Parent:
#     def __init__(self):
#         print("Parent")
#
# class Child(Parent):
#     def __init__(self):
#         print("Child")
# Результат:
# Parent
# Child


# Описание:
# Требуется реализовать функцию, которая будет искать повторяющиеся числа в списке.
# Числа, значению записаны в виде list.
# Результат вывести на экран.

# Входные данные:
v = [1, 2, 3, 2, 4, 1, 5, 2]

# Результат:
# (1, 2)

# • pytest — запускает все тесты по умолчанию
# • pytest test_file.py — запустить тесты только из указанного файла
# • pytest test_file.py::TestClass::test_method — запустить конкретный тестовый метод в классе
# • pytest -v — подробный (verbose) вывод результатов тестов
# • pytest -k "строка" — запуск тестов по имени (паттерн в имени теста)
# • pytest -m markname — запуск тестов с определённой меткой (mark)
# • pytest --maxfail=3 — остановить после 3 первых неудачных тестов
# • pytest --tb=short — короткий формат вывода traceback ошибок
#
#
# • Часто используется просто pytest или с опцией -v для подробностей
# • Для интеграции с CI (например, GitLab CI) команды обычно прописывают в .gitlab-ci.yml, например:

# script:
#     - pytest -v --maxfail=1

import pytest
#
# order = []
#
# @pytest.fixture(scope='session')
# def s1():
#     order.append('s1')
#
# @pytest.fixture(scope='module')
# def m1():
#     order.append('m1')
#
# @pytest.fixture()
# def f3():
#     order.append('f3')
#
# @pytest.fixture(scope='session', autouse=True)
# def a1():
#     order.append('a1')
#
# @pytest.fixture()
# def f2():
#     order.append('f2')
#
# @pytest.fixture()
# def f1(f3):
#     order.append('f1')
#
# def test_order(f1,m1,f2,s1):
#     assert order == ['a1','s1','m1','f3', 'f1', 'f2']


# кратно 2 = "би"
# кратно 7 = "зон"
# кратно 2и7 = "бизон"


# for n in range(1, 101000):
#     if n % 2 == 0 and n % 7==0:
#         print('bizone')
#     elif n % 7==0:
#         print('zone')
#     elif n % 2==0:
#         print('bi')
#     else:
#         print(n)

#
# def my_generate():
#     count = 1
#     while True:
#         yield count
#         count += 1
#
# g = my_generate()
#
# for n in range(1,5):
#     print(next(g))


# 200 при успехе
# отдает адрес ip
# и сообщение по свагеру

import pytest
import requests
import socket

def test_get_ip():
    url='https://httpbin.dmuth.org/ip'
    response = requests.get(url,timeout=2)
    hostname = socket.gethostname()  # получаем имя хоста
    ip_address = socket.gethostbyname(hostname)  # преобразуем в IP
    data = response.json()
    current_ip = data['ip']
    assert response.status_code == 200
    assert ip_address == current_ip
    assert 'message' in data
    assert data['message'][0] == "If you're looking for v4 or v6 specific endpoints, try /ip/v4 or /ip/v6."
    assert data['message'][1] == "If you want to ping this IP and graph the results, I built an app for that too: https://github.com/dmuth/grafana-network-monitor"

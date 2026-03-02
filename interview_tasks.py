#TODO Вернуть True если палиндром
#'abba' == True / 'racecar' == True / 'boom' ==  False
from pygame.examples.go_over_there import reset


def is_palindrome(s:str)-> bool:
    """Время O(n) Память O(n)"""
    return s == s[::-1]

def is_palindrome_improved(data:str)->bool:
    """Игнорирует пробелы, регистр и знаки препинания"""
    result = ''
    for char in data.lower():
        if char.isalnum():
            result += char
    return result == result[::-1]

def is_palindrome_improved_method_two(s:str)->bool:
    """Через list comprehension"""
    s = [ch for ch in s.lower() if ch.isalpha()]
    return s == s[::-1]

#print(is_palindrome_improved_method_two("Do geese see God?"))



#TODO Написать авто-тест на какой-то URL, который будет проверять статус-код. По ходу: вынести URL в fixture

import pytest
import requests


# Базовый урл вынесен в fixture, чтобы переиспользовать кода и упростить поддержку кода (confTest.py)
@pytest.fixture
def base_url():
    return 'https://ya.ru'

STATUS_CODE_OK = 200 # Константы вынесем в helpers/const

# Сам тест пишем в tests/test_status_code.py и можно добавить еще таймаут
def _test_base_url_returns_200(base_url):
    response = requests.get(base_url, timeout=5) # таймаут здесь как защита от зависаний (requests.exceptions.Timeout)
    assert response.status_code == STATUS_CODE_OK, 'status code is not OK'
    assert response.elapsed.total_seconds() < 2, 'response is to slow' # а это проверка времени ответа (testing fail)



#TODO Написать функцию, в которую можно передавать аргументы, вывод — сложение чисел.
#Далее - улучшить под любое количество чисел; написать декоратор, умножающий вывод на 2.


def decorator_x2(func):
    """Декоратор - это паттерн проектирования.
    Используется, чтобы изменить поведение функции / класса без изменения их исходного кода.
    Фактически, это функция, которая принимает функцию и возвращает новую функцию"""
    def wrapper(*args):
        print('log')
        return func(*args) * 2
    return wrapper

@decorator_x2 # Это значит summator = decorator_x2(summator)
def summator(*args:int)->int:
    return sum(args)

#print(summator(4,8,2,3))


def decorator_with_param(n=123):
    """Для проброса параметров нужно добавить еще вложенность и возвращать (не вызывая) обертки"""
    def decorator(func):
        def wrapper(*args):
            result = func(*args) * n
            return result
        return wrapper
    return decorator


@decorator_with_param(4) #аналог get_summ = decorator_with_param(2)(get_summ)
def get_summ(*args:int)->int:
    return sum(args)

#print(get_summ(1,2,4))


#TODO декоратор который делает retry 3 раза, если функция упала с exception.

def retry(retries=3):
    def decorator(func):
        def wrapper(*args):
            last_exception = None

            for attempt in range(retries):
                try:
                    return func(*args)
                except Exception as e:
                    last_exception = e
                    print(f'Attempt {attempt} result: {e}')
            print("STOP RETRY")
            raise last_exception
        return wrapper
    return decorator


@retry(4)
def unstable_func(*str):
    result = str
    raise TypeError("Something wrong")


#print(unstable_func(3))


#TODO вернуть отсортированный список уникальных квадратов из строки for WB

def get_unic_squares(data:str)->list:
    result = set()

    for el in data.split():
        try:
            n = int(el)
            result.add(n*n)
        except ValueError:
            pass

    return sorted(result)

print(get_unic_squares('sdjk 82 ksjdf l 8 24 -2'))
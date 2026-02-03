#примеры использования lambda функций (короткая безымянная функция, которую мы не хотим именовать)
from os import rename

a = {
    1: 13,
    2: 24,
    3: 22
}

print(max(a)) # Получим самый большой ключ
print(max(a, key= lambda x: a[x])) # Вернет самое большое значение



# Рекурсия. Это когда функция вызывает сама себя
# Предпочтительнее использовать цикл - это более оптимизированный подход, хоть и выглядит не так элегантно
# Дефолтный лимит глубины рекурсии в Питоне = 1000. Далее - ошибка


def factorial_rec(n):
    if n == 1:
        return n
    else:
        return n * factorial_rec(n-1)

def factorial_base(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n-1
    return num

import sys
print(sys.getrecursionlimit()) # Проверяем лимит глубины рекурсии
sys.setrecursionlimit(333) # Так можно установить лимит глубины рекурсии
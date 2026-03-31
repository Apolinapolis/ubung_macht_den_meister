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

new = Child()


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
# Требуется реализовать вывод функции print 2х классов: Parent, Child.
# При двух ограничениях: 1 - нельзя писать вывод Parent класса прямым текстом. 2 - нельзя менять наследуемость класса Child
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
# [1, 2, 3, 2, 4, 1, 5, 2]

# Результат:
# (1, 2)
from datetime import datetime
# Пример класса и его экземпляра

class Person:
    name: str # Аннотация типа (Так принято)
    last_name: str
    class_attr = 'атрибут класса' # Меняя его, меняем значение во всех экземплярах

    # Метод инициализации объекта (не создает объект, а только инициализирует)
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.class_attr = 3 #Атрибут объекта. Можно назвать как и атрибут класса, они друг другу не мешают

    def __str__(self):
        # Магические методы обычно вызываются встроенными функциями: str(obj) вызывает str().
        return self.name

    # Метод экземпляра класса. Можно вызвать только создав экземпляр
    def say_hi(self):
        print(f'hello! My name is {self.name}')

    # Метод класса принадлежит всему классу и позволяет вызвать метод без создания экземпляра класса
    @classmethod
    def get_my_workplace(slc):
        return slc.class_attr

    # Статический метод тоже можно вызывать из класса и из экземпляра, но он не получает аргумент и ломает полиморфизм
    @staticmethod
    def get_current_time():
        return datetime.now()

    @property # теперь функция будет вызываться как атрибут и динамически вычислять значение
    def full_name(self):
        return f'{self.last_name} {self.name}'

    @full_name.setter
    def full_name(self, value):
        name_surname = value.split(' ')
        self.name, self.last_name = name_surname


    public = 'pass' # Публичный метод
    _protected = 'password' # Договоренность о подчеркивании
    __private = 'mangling' # Вызывается Person._Person__private (имя искажается питоном)


ob = Person('dimon','top')
print(Person.class_attr)
print(ob.class_attr)
Person.get_current_time()
ob.get_current_time()
di = Person('Dima', 'Best')
print(di.full_name)
# Person._Person__private()

di.full_name = 'changed surname'
print(di.name)
print(di.last_name)
print(Person.public)
print(Person._protected)
print(ob._protected)

ob.__str__()

# for tech screening
class C:
    pass

a = C()
b = C()
#print(a == b) # 1)false если класс не переопределяет __eq__ то == здесь работает как is
a = b = C()
#print(a == b) # 2)true - ссылаются на один объект в памяти

#TODO Вызвать все методы класса (from myFlower)

class A:

    def __init__(self):
        self.text = None

    def __str__(self):
        return self.text

    @staticmethod
    def what_time():
        return f'current time'

    @property
    def useless_getter(self):
        return self.text

    def __private_or_public(self):
        return 1
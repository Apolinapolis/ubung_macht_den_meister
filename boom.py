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

print(summarize_result(statuses))


# Вариант через импорт
from collections import Counter

def summarize_result_two(data:str)->dict:
    return dict(Counter(x.strip() for x in data.split(',')))

print(summarize_result_two(statuses))



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
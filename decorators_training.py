def strong(func):
    def wrap():
        return '<strong>'+ func() + '</strong>'
    return wrap

def italic(func):
    def wrap():
        return '<italic>'+ func() + '</italic>'
    return wrap

def base_text_generator(text):
    return text


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'trace calling {func.__name__} function! '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'trace original: {func.__name__} '
              f'returned: {original_result}')
        return original_result
    return wrapper


import functools

def retry(func, times):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        counter = 0
        while counter < times:
            try:
                result = func(*args, **kwargs)
            except:
                counter += 1
        return result
    return wrapper

import re

# @retry(times=3)
# def my_function(name, job):
#     return f'{name} - {job}'

# def logger(f):
#     def wrapper(*args, **kwargs):
#         print('i"m observing')
#         return f(*args, **kwargs)
#     return wrapper
#
# def greet(*args, **kwargs):
#     print(f"Привет, {args} & {kwargs}")
#
# decorated = logger(greet)
# decorated('ops', 'uo','kamon', named='baba', name='deda')

# def logger(f):
#     def wrapper(*args,**kwargs):
#         print(f'function {f.__name__} is called!')
#         print(f'with args:{args}')
#         print(f'and kwargs:{kwargs}')
#         return f(*args, **kwargs)
#     return wrapper
#
# @logger
# def power(base, exp=2):
#     return base ** exp
#
# print(power(3, exp=4))


if __name__ == "__main__":


   def filter_even(data):
       return [n for n in data if not n%2]

   print(filter_even([1,2,3,4,5,6,7,8]))

   def find_diff(numbers):
       min_value = numbers[0]
       max_value = numbers[0]
       for n in numbers:
           if n < min_value:
               min_value = n
           if max_value < n:
               max_value = n
       return max_value - min_value

   print(find_diff([66,33]))

   def find_anagram(word_1,word_2):
       counter_word_1 = {}
       counter_word_2 = {}

       for ch in word_1:
           counter_word_1[ch] = counter_word_1.get(ch, 0) + 1
       for ch in word_2:
           counter_word_1[ch] = counter_word_2.get(ch, 0) + 1

       return counter_word_2 == counter_word_1

   print(find_anagram("listenz" ,"si6lent")) # wrong :(


   def flatten(elem):
       result = []
       for el in elem:
           if isinstance(el, list):
               result.extend(flatten(el))
           elif isinstance(el, int):
               result.append(el)
       return result


   print(flatten([1, [2, 3], [4, [5, 6]]])) # wrong :(


  # def cleaner(numbers):
  #     return list(set(numbers))
  #
  # print(cleaner([1,2,3,1,2,4]))
  #
  # def new_revers(str):
  #     result = ''
  #     for ch in str:
  #         result = ch + result
  #     return result
  #
  # print(new_revers('hello'))
  #
  # def find_palindrom(str):
  #     base_word = str
  #     reverse_word = str[::-1]
  #     return base_word == reverse_word
  #
  # print(find_palindrom('boom'))



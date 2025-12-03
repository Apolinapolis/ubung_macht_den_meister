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


# @retry(times=3)
# def my_function(name, job):
#     return f'{name} - {job}'




if __name__ == "__main__":
    def logger(f):
        def wrapper(*args, **kwargs):
            print('i"m observ')
            return f(*args, **kwargs)
        return wrapper

    def greet(*args, **kwargs):
        print(f"Привет, {args} & {kwargs}")

    decorated = logger(greet)
    decorated('ops', 'uo','kamon', named='baba', name='deda')


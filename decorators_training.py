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


if __name__ == "__main__":

    @strong
    @italic
    def my_text():
        return 'i am the best'

    print(my_text())
class File:
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


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")


class C(A):
    def __init__(self):
        super().__init__()
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

print(D()) # A-C-B-D


import pytest

@pytest.fixture
def foo(request):
    param = request.params.get('param_name')
    pass

@pytest.mark.parametrize('param_name', [...], indirect=True)
def test_func(foo):
    pass
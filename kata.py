class File:
    """Итератор"""
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
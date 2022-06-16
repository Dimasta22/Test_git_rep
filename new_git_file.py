class GitFile:
    def __init__(self, height, age):
        self.height = height
        self.age = age

    def animal(self):
        return f'{self.height}, {self.age}'

    def owner(self):
        return f'{self.height}, {self.age}'

class Test:
    def __init__(self, street):
        self.street = street

    def check(self):
        return f'{self.street}'



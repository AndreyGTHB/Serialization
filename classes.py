class Person:
    def __init__(self, name = "John", age = 10):
        self.name = name
        self.age = age

    def method(self):
        print("It is method of " + str(self.__class__.__name__))
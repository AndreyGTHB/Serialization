from Serialization import *


class A:
    def __init__(self):
        self.num = 1
        self.second_num = 5

    def method(self):
        pass


class B(A):
    def __init__(self):
        super(B, self).__init__()

        self.ob = A()


print(Serialization.get_json_object(B()))


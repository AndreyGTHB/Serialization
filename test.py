from Serialization import Serialization as ser
import json


class A:
    def __init__(self):
        self.num = 1
        self.second_num = 5

    def method(self):
        pass


a = A()


class B(A):
    def __init__(self):
        super(B, self).__init__()

        self.ob = a


b = B()

ser.save_to_file(a, "test1.json", True)
ser.save_to_file(b, "test1.json")



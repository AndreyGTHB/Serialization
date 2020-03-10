from Serialization import Serialization as ser
import json


class A:
    def __init__(self):
        self.num = 1
        self.second_num = 5
		
        self.obj = self

    def method(self):
        pass


a = A()

ser.save_to_file(a, "test1.json", True)

print(id(a))




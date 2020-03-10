import json

from Serialization import Serialization as ser


class A:
    def __init__(self):
        self.num = 1
        self.second_num = 5

    def method(self):
        print("It is method of " + str(self.__class__.__name__))


a = A()

ser.save_to_file(a, "test1.json", True, False)

with open("test1.json", "r") as file_object:
    json_obj = json.load(file_object)

    py_obj = ser.get_py_object(json_obj, "test")
    for key in json_obj:
        print(key + ': ' + str(py_obj.key))

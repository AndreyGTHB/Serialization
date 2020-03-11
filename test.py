import json

from Serialization import Serialization as ser
from classes import Person


a = Person("Andrey", 11)

ser.save_to_file(a, "test1.json", True, False)

with open("test1.json", "r") as file_object:
    json_obj = json.load(file_object)

    py_obj = ser.get_py_object(json_obj, "classes")
    for key in json_obj:
        print(key + ': ' + str(getattr(py_obj, key))) # Throw the AttributeError

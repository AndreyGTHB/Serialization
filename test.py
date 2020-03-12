import json

from Serialization import Serialization as ser
from classes import Person


a = Person("Andrey", 11)

ser.save_to_file(a, "test1.json", True, False)

print(ser.load_object_from_file("test1.json", "classes"))

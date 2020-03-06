import json


class Serializable:
    def __init__(self, format, path_to_file):
        self.format = format
        if self.format is None:
            self.format = "txt"

        self.path_to_file = path_to_file

    def change_file(self, path_to_file):
        self.path_to_file = path_to_file

    def read_file(self):
        with open(self.path_to_file, "r") as file_object:
            if self.format == "txt":
                ans = file_object.read()
            else:
                ans = json.load(file_object)
        return ans

    def serialize(self):
        with open(self.path_to_file, "w") as file_object:
            if self.format == "json":
                json.dump(self, file_object)

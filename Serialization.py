import abc
import json


class Serialization(abc.ABC):
    population = 0
    links = []

    @staticmethod
    def get_json_object(obj, use_id=False, to_string=False):
        if use_id:
            for link in Serialization.links:
                if obj == link[0]:
                    return "$&%_@link_id=" + str(link[1])

        Serialization.links.append((obj, id(obj)))

        dict_of_obj = obj.__dict__

        dict_of_obj['$&%_id'] = id(obj)
        dict_of_obj['$&%_class'] = str(obj.__class__.__name__)
        Serialization.population += 1

        for key in dict_of_obj:
            if "__main__." in str(dict_of_obj[key]) and "object at" in str(dict_of_obj[key]):
                dict_of_obj[key] = Serialization.get_json_object(dict_of_obj[key], True)

        if to_string:
            return json.dumps(dict_of_obj)

        return dict_of_obj

    @staticmethod
    def save_to_file(obj: object, path_to_file: str, clear_file: bool = False, use_id: bool = True) -> None:
        obj_dict = Serialization.get_json_object(obj, use_id)

        if clear_file:
            with open(path_to_file, "w") as file_object:
                json.dump(obj_dict, file_object)
                return

        with open(path_to_file, "r") as file_object:
            obj_from_file = json.load(file_object)

        if type(obj_from_file) != list:
            obj_from_file = [obj_from_file]
        obj_from_file.append(obj_dict)

        with open(path_to_file, "w") as file_object:
            json.dump(obj_from_file, file_object)

    @staticmethod
    def get_py_object(json_object: dict, module: str):
        """
        This method will not work
         if there are no default values
         for the arguments in the constructor
         of the deserialized class.
        """

        def my_import(name):
            components = name.split('.')
            mod = __import__(components[0])
            for comp in components[1:]:
                mod = getattr(mod, comp)
            return mod

        klass = my_import(f"{module}.{json_object['$&%_class']}")
        py_obj = klass()

        for key in json_object:
            if key != "$&%_id" and key != "$&%_class":
                setattr(py_obj, key, json_object[key])

        return py_obj

    @staticmethod
    def load_object_from_file(path_to_file: str, module_with_class: str):
        with open(path_to_file, 'r') as file_obj:
            json_obj = json.load(file_obj)
        py_object = Serialization.get_py_object(json_obj, module_with_class)

        return py_object












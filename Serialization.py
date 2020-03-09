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
                    return "$#&% @ser ?obj " + "id=" + str(link[1])

        Serialization.links.append((obj, Serialization.population))

        dict_of_obj = obj.__dict__

        dict_of_obj['id'] = Serialization.population
        dict_of_obj['class'] = str(obj.__class__.__name__)
        Serialization.population += 1

        for key in dict_of_obj:
            if "__main__." in str(dict_of_obj[key]) and "object at" in str(dict_of_obj[key]):
                dict_of_obj[key] = Serialization.get_json_object(dict_of_obj[key], True)

        if to_string:
            return json.dumps(dict_of_obj)

        return dict_of_obj

    @staticmethod
    def save_to_file(obj, path_to_file, clear_file=False, use_id=True):
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

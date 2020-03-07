import abc
import json


class Serialization(abc.ABC):
    population = 0

    @staticmethod
    def get_json_object(obj, to_string=True):
        dict_of_obj = obj.__dict__

        dict_of_obj['id'] = Serialization.population
        dict_of_obj['class'] = str(obj.__class__.__name__)
        Serialization.population += 1

        for key in dict_of_obj:
            if "__main__." in str(dict_of_obj[key]) and "object at" in str(dict_of_obj[key]):
                dict_of_obj[key] = "object"

        if to_string:
            return json.dumps(dict_of_obj)

        return dict_of_obj

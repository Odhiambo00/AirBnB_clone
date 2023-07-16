#!/usr/bin/python3

"""FileStorage class module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class FileStorage"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary `__objects`"""

        return self.__objects

    def new(self, obj):
        """Sets in `__objects` the `obj` with key `<obj class name>.id`"""

        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes `__objects` to the JSON file (path: `__file_path)`"""

        serialized_obj = {}

        for k, v in self.__objects.items():
            serialized_obj[k] = v.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """
        Deserializes the JSON file `__file_path` `to __objects` if
        it exists
        """

        c_list = {
                'BaseModel': BaseModel,
                'User': User,
                'Amenity': Amenity,
                'Place': Place,
                'City': City,
                'State': State,
                'Review': Review
                }

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                serialized_obj = json.load(f)

            for k, v in serialized_obj.items():
                class_name, obj_id = k.split('.')
                self.__objects[k] = globals()[class_name](**v)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    storage = FileStorage()
    storage.reload()

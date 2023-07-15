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

        return FileStorage.__objects

    def new(self, obj):
        """Sets in `__objects` the `obj` with key `<obj class name>.id`"""

        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes `__objects` to the JSON file (path: `__file_path)`"""

        serialized_obj = FileStorage.__objects
        serialized_obj = {obj: serialized_obj[obj].to_dict() for obj
                          in serialized_obj.keys()}

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """
        Deserializes the JSON file `__file_path` `to __objects` if
        it exists
        """

        try:
            with open(FileStorage.__file_path) as f:
                serialized_obj = json.load(f)

            for k, v in serialized_obj.items():
                class_name = v['__class__']
                del v['__class__']
                self.new(eval(class_name)(**v))
        except FileNotFoundError:
            pass

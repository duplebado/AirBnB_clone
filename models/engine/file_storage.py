#!/usr/bin/python3
""" Defines a class 'FileStorage' that serializes instances
    to a JSON file and deserializes JSON file to instances
"""

import json


class FileStorage:
    """
        serializes instances to a JSON file and deserializes
        JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            get all __objects

            Returns
            -------
                __objects : dict
                    all __objects
        """
        
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the property with key <obj class name>.id
            and value 'obj'

            Parameters
            ----------
                obj
        """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
            serialize __objects to the JSON file
        """

        with open(self.__file_path, mode="w") as f:
            dict_store = {}
            for k, v in self.__objects.items():
                dict_store[k] = v.to_dict()
            json.dump(dict_store, f)

    def reload(self):
        """
            deserializes the JSON file to __objects
            only IF it exists
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                stored_dict = json.load(f)
                for obj in stored_dict.values():
                    self.new(json.loads(obj))

            print("length of objs", len(self.__objects))
        except:
            pass

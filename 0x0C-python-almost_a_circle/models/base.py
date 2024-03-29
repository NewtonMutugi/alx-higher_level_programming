#!/usr/bin/python3
"""Base class for all other classes in this project"""

import json
import os
import csv


class Base:
    """Base class for all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the list of objects to a file"""
        import json
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs]))
                return filename
            return None

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation json_string"""
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        import json
        filename = cls.__name__ + ".json"

        if os.path.exists(filename):
            with open(filename, "r") as f:
                return [cls.create(**obj) for obj in
                        cls.from_json_string(f.read())]
        else:
            return []
        # try:
        #     with open(filename, "r") as f:
        #         return [cls.create(**obj) for obj in
        #                 cls.from_json_string(f.read())]
        # except FileExistsError:
        #     return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the list of objects to a file"""
        import csv
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
                return filename
            return None

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances"""
        import csv
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                return [cls.create(**{k: int(v) for k, v in
                                      obj.items()})
                        for obj in reader]
        else:
            return []

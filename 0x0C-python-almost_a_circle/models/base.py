#!/usr/bin/python3
"""Base class for all other classes in this project"""


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


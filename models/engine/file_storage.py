#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

classes = {"User": User}

class FileStorage:
    __filepath = "file.json"
    __objects = {}

    def new(self, obj):
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def all(self, cls=None):
        if cls:
            new = {}
            for key, val in self.__objects.items():
                if cls == self.__class__ or cls == self.__class__.__name__:
                    new[key] = val
            return new
        return self.__objects

    def save(self):
        json_obj = {}
        for key in self.__objects.keys():
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__filepath, "w") as f:
            json.dump(json_obj, f)

    def reload(self):
        try:
            with open(self.__filepath, "r") as f:
                jo = json.load(f)
            for key in jo:
                cls = classes[jo[key]["__class__"]]
                self.__objects[key] = cls(**jo[key])
        except Exception:
            pass

    def delete(self, obj=None):
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def get(self, cls, id):
        for val in classes.values():
            if cls not in classes.values():
                return None
            key = cls.__name__ + "." + id
            for k in self.__objects:
                if k == key:
                    return self.__objects[key]
        return None

    def close():
        self.reload()

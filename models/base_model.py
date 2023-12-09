#!/usr/bin/python3
import uuid
import models
from datetime import datetime
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


if getenv("STORAGE_TYPE") == "db":
    Base = declarative_base()
else:
    Base = object


time = "%Y-%m-%d %H:%M:%S.%f"


class BaseModel:
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    setattr(self, key, val)
                if kwargs.get("id") is None:
                    self.id = str(uuid.uuid4())
                if kwargs.get("created_at"):
                    self.created_at = datetime.strptime(kwargs["created_at"], (time))
                else:
                    self.created_at = datetime.now()
                if kwargs.get("updated_at"):
                    self.updated_at = datetime.strptime(kwargs["updated_at"], (time))
                else:
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return "[{}] [{}] {}".format(
            self.__class__.__name__, self.id,
            self.__dir__)

    def save(self):
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        new = self.__dict__.copy()
        if "created_at" in new:
            new["created_at"] = new["created_at"].strftime(time)
        if "updated_at" in new:
            new["updated_at"] = new["updated_at"].strftime(time)
        new["__class__"] = self.__class__.__name__
        if new.get("_sa_instance_state"):
            del new["_sa_instance_state"]
        if "password" in new:
            del new["password"]
        if "oauth_user_id" in new:
            del new["oauth_user_id"]
        return new

    def delete(self):
        models.storage.delete(self)

    def count(self):
        models.storage.count(self)

#!/usr/bin/python3
from os import getenv


storage_t = getenv("STORAGE_TYPE")

if storage_t == "db":
    from models.engine.db import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

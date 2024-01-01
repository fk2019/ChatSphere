#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.user import User
from models.message import Message
from models.conversation import Conversation
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from dotenv import load_dotenv

load_dotenv()

classes = {"User": User, "Message": Message, "Conversation": Conversation}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        DB_USER = getenv("DB_USER")
        DB_PWD = getenv("DB_PWD")
        DB_HOST = getenv("DB_HOST")
        DB_DB = getenv("DB_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_DB))

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def new(self, obj):
        #del obj._sa_instance_state
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def all(self, cls=None):
        new = {}
        for cl in classes:
            if cls is None or cls is cl or cls is classes[cl]:
                objs = self.__session.query(classes[cl]).all()
                for ob in objs:
                    key = ob.__class__.__name__ + "." + ob.id
                    new[key] = ob

        return new

    def delete(self, obj=None):
        if obj:
            for conv in obj.conversations:
                for m in conv.messages:
                    del m
                del conv
            print(obj.conversations)
            self.__session.delete(obj)

    def get(self, cls, id):
       for cl in classes:
            if cls is classes[cl]:
                objs = self.__session.query(cls).all()
                for ob in objs:
                    if ob.id == id:
                        return ob
        #return None

    def close(self):
        self.__session.remove()

    def count(self, cl=None):
        count = 0
        for cls in classes:
            if cl is classes[cls] or cl is cls:
                ob = self.__session.query(classes[cls]).all()
                return len(ob)

        ob = self.__session.query(cls).all()
        count += len(ob)
        return count

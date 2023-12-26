#!/usr/bin/python3
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Message(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = "messages"
        content = Column(String(1024))
        filepath = Column(String(128))
        isFile = Column(String(60))
        conversation_id = Column(String(60), ForeignKey('conversations.id'))
        conversation = relationship('Conversation', back_populates='messages')
        sender_id = Column(String(60), ForeignKey('users.id'))
        timestamp = Column(String(60))
    else:
        first_name = ""
        last_name = ""
        email = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

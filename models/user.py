#!/usr/bin/python3
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


participants_table = Table(
    'participants',
    Base.metadata,
    Column('user_id', String(60), ForeignKey('users.id')),
    Column('conversation_id', String(60), ForeignKey('conversations.id')),
    Column('last_read_message_id', String(60))
)


class User(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = "users"
        user_name = Column(String(128), nullable=False)
        password = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)
        profile_photo = Column(String(128), default='/home/francis/Drop/Test_v2/default_images/dog.jpg')
        oauth_provider = Column(String(60))
        oauth_user_id = Column(String(60))
        conversations = relationship(
            'Conversation', secondary=participants_table,
            back_populates='participants')

    else:
        first_name = ""
        last_name = ""
        email = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

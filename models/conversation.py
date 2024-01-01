#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.user import participants_table
import models
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Conversation(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = "conversations"
        participants = relationship(
            'User', secondary=participants_table,
            back_populates='conversations')
        last_read_message_id = Column(String(60))
        messages = relationship('Message', back_populates='conversation')
    else:
        first_name = ""
        last_name = ""
        email = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_participant(self, user):
        """add unique participants"""
        if user not in self.participants:
            self.participants.append(user)

    def mark_as_read(self, user_id, last_message_id):
        """Mark messages as read"""
        participant = next(p for p in self.participants if p.id == user_id)
        participant.last_read_message_id = last_read_message_id

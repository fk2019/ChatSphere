#!/usr/bin/python3
from models.user import User
from models.message import Message
from models.conversation import Conversation
from models import storage
from datetime import datetime
from flask import jsonify
import time

ftime = "%H:%M:%S  %d %b %y"
kwargs = {"user_name": "shin", "email": "fkmuiruri8@gmail.com", "password": "shin86"}
kwargs2 = {"user_name": "chopper", "email": "chopperdoc@north.com", "password": "reindeer"}
kwargs3 = {"user_name": "john", "email": "puppy@continental.org", "password": "puppy"}
kwargs4 = {"user_name": "ragna", "email": "ragna@oblivion.society", "password": "dragonhunter01"}


def create_users():
    users = [kwargs, kwargs2, kwargs3, kwargs4]
    us = []
    for user in users:
        u = User(**user)
        u.save()
        us.append(u)
    return us


def main():
    users = create_users()
    us1 = users[0]
    us2 = users[1]
    conv1 = Conversation()
    post = {"content": "DSA may sound provocative on first encounter. However, ALX made it appear easy, of course after working really hard.", "conversation_id": conv1.id, "sender_id": us1.id}
    # msg = Message(**post)
    # msg.save()

    conv1.add_participant(us1)
    conv1.add_participant(us2)
    conv1.add_participant(us2)
    #conv1.messages.extend([Message(**post)])
    conv1.save()
    print(us1.id, us2.id)
    print(conv1.__dir__())
    p = [u for u in conv1.participants]
    print(conv1.to_dict())



    post2 = {'content': 'Anime is a style of animation that originated in Japan and has become popular worldwide.'}
    post3 = {'content': 'History is the study of past events, particularly in human affairs and societies.'}
    post4 = {'content': 'Science is the systematic study of the natural world, and technology refers to the application of scientific knowledge for practical purposes.'}


main()

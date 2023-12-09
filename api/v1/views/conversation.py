#!/usr/bin/python3
"""New view for  User objects"""
from api.v1.views import app_views
from flask import abort, request, make_response, jsonify
from models import storage
from models.user import User
from models.message import Message
from models.conversation import Conversation


@app_views.route('/users/conversations/<string:user_id>/', strict_slashes=False)
def conversations(user_id):
    """Retrieve list of all Conversation objects"""
    result = []
    obj = storage.get(User, user_id)
    if obj is None:
        abort(404)
    for conversation in obj.conversations:
        result.append(conversation.to_dict())
    return (jsonify(result))


@app_views.route('/conversations/<string:user1_id>/<string:user2_id>', strict_slashes=False)
def get_conversation(user1_id, user2_id):
    """Retrieve a Conversation object by participants"""
    convs = storage.all(Conversation)
    for conv in convs.values():
        participants_ids = [p.id for p in conv.participants]
        if user1_id in participants_ids and user2_id in participants_ids:
            return conv.id
        abort(404)


@app_views.route('/conversations/<string:conversation_id>/', strict_slashes=False)
def conversation(conversation_id):
    """Retrieve a Conversation object"""
    obj = storage.get(Conversation, conversation_id)
    if obj:
        return obj.to_dict()
    else:
        abort(404)


@app_views.route('/conversations/', methods=['POST'], strict_slashes=False)
def create_conversation():
    """Add a Conversation object"""
    data = request.get_json()
    if not data:
        return (make_response(jsonify({'error': 'Not a JSON'})))
    user1_id = data.get('participants')[0]
    user2_id = data.get('participants')[1]
    user1 = storage.get(User, user1_id)
    user2 = storage.get(User, user2_id)
    conv = Conversation()
    conv.add_participant(user1)
    conv.add_participant(user2)
    conv.save()
    c = storage.get(Conversation, conv.id)
    del conv.participants
    conv.participant = [user1_id, user2_id]
    return conv.to_dict()

#!/usr/bin/python3
"""New view for  Message objects"""
from api.v1.views import app_views
from flask import abort, request, make_response, jsonify, send_from_directory, current_app
from models import storage
from models.user import User
from models.message import Message
from models.conversation import Conversation
import os
from werkzeug.utils import secure_filename

@app_views.route('/conversations/<string:conversation_id>/messages', strict_slashes=False)
def messages(conversation_id):
    """Retrieve list of all sent Message objects"""
    result = []
    obj = storage.get(Conversation, conversation_id)
    if obj is None:
        abort(404)
    for message in obj.messages:
        result.append(message.to_dict())
    result = sorted(result, key=lambda k: k['updated_at'])
    return (jsonify(result))


@app_views.route('/conversations/<string:conversation_id>/messages', methods=['POST'], strict_slashes=False)
def post_message(conversation_id):
    """Post a Message object"""
    args = ['content', 'sender_id']
    if not request.get_json():
        return (make_response(jsonify({'error': 'Not a JSON'}), 400))
    for arg in args:
        if arg not in request.get_json():
            return (make_response(jsonify({'error': 'Missing {}'.format(arg)}), 400))

    conv = storage.get(Conversation, conversation_id)
    if not conv:
        abort(404)
    conv.messages.append(Message(**request.get_json()))
    conv.save()
    if conv:
        return (jsonify({"status": "message sent successfully"}), 201)
    abort(404)


@app_views.route('/conversations/<string:conversation_id>/<string:sender_id>/messages/file', methods=['POST'], strict_slashes=False)
def post_message_image(conversation_id, sender_id):
    """Post a Message object with file"""
    if 'file' not in request.files:
        return (make_response(jsonify({'error': 'No file selected'})), 400)
    file = request.files.get('file')
    filename = file.filename
    filename = secure_filename(filename)
    content_type = file.content_type
    folder = current_app.config.get('UPLOAD_FOLDER')
    path = os.path.join(folder, filename)
    file.save(path)
    data = {'file': filename, 'sender_id': sender_id}
    conv = storage.get(Conversation, conversation_id)
    if not conv:
        abort(404)
    conv.messages.append(Message(**data))
    conv.save()
    if conv:
        return (jsonify({"status": "file uploaded successfully"}), 200)
    abort(404)


@app_views.route('/conversations/<string:conversation_id>/file/<string:file_name>', strict_slashes=False)
def message_file(conversation_id, file_name):
    """Retrieve message file"""
    obj = storage.get(Conversation, conversation_id)
    if obj is None:
        abort(404)
    filename = secure_filename(file_name)
    folder = current_app.config.get('UPLOAD_FOLDER')
    return (send_from_directory(folder, filename), 200)

@app_views.route('/conversations/<string:conversation_id>/messages/<string:message_id>', methods=['DELETE'], strict_slashes=False)
def delete_message(conversation_id, message_id):
    """Delete a Message object for all"""
    conv = storage.get(Conversation, conversation_id)
    if not conv:
        abort(404)
    msg = storage.get(Message, message_id)
    if msg:
        msg.delete()
        storage.save()
        return ([], 201)
    abort(404)

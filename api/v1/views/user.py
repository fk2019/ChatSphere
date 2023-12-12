#!/usr/bin/python3
"""New view for  User objects"""
from api.v1.views import app_views
from flask import abort, request, make_response, jsonify, send_from_directory, current_app
from models import storage
from models.user import User
from models.redis import redis_client
import os
from io import BytesIO
from werkzeug.utils import secure_filename


@app_views.route('/users', strict_slashes=False)
def users():
    """Retrieve list of all User objects"""
    result = []
    obj = storage.all(User)
    if obj is None:
        abort(404)
    for val in obj.values():
        user = val.to_dict()
        user["conversation_ids"] = [c.id for c in val.conversations]
        result.append(user)
    return (jsonify(result))


@app_views.route('/users/<string:user_id>', strict_slashes=False)
def user(user_id):
    """Retrieve a User object"""
    obj = storage.get(User, user_id)
    if obj:
        user = obj.to_dict()
        user["conversation_ids"] = [c.id for c in obj.conversations]

        return user
    else:
        abort(404)


@app_views.route('/users/<string:user_id>/image', strict_slashes=False)
def user_image(user_id):
    """Retrieve a User object's image"""
    if redis_client.exists(user_id):
        obj = redis_client.get(user_id).decode('utf-8')
        obj = eval(obj)
    else:
        obj = storage.get(User, user_id)
        if not obj:
            abort(404)
        obj = obj.to_dict()
        redis_client.set(user_id, str(obj))
    filename = obj.get('profile_photo')
    folder = current_app.config.get('UPLOAD_FOLDER')
    return (send_from_directory(folder, filename), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Post a User object"""
    basic_args = ['user_name', 'email', 'password']
    oauth_args = ['user_name', 'email', 'oauth_provider', 'oauth_user_id']
    if not request.get_json():
        return (make_response(jsonify({'error': 'Not a JSON'}), 400))
    if 'oauth_provider' in request.get_json():
        save_user(oauth_args)
    save_user(basic_args)

def save_user(args):
    """Save user in db"""
    for arg in args:
        if arg not in request.get_json():
            return (make_response(jsonify({'error': 'Missing {}'.format(arg)}), 400))
    obj = User(**request.get_json())
    if not obj:
        abort(404)
    obj.save()
    return (obj.to_dict(), 201)


@app_views.route('/users/<string:user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update a User object"""
    obj = storage.get(User, user_id)
    if not request.get_json():
        return (make_response(jsonify({'error': 'Not a JSON'}), 400))
    elif obj is None:
        abort(404)
    else:
        for key, val in request.get_json().items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(obj, key, val)
        obj.save()
        return (obj.to_dict(), 200)


@app_views.route('/users/<string:user_id>/upload', methods=['PUT'], strict_slashes=False)
def update_user_pic(user_id):
    """Update a User object's image"""
    upload_folder = current_app.config.get('UPLOAD_FOLDER')
    obj = storage.get(User, user_id)
    ALLOWED_EXTS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    if not obj:
        abort(404)
    if 'image' not in request.files:
        return (make_response(jsonify({'error': 'No file selected'})), 400)
    file = request.files.get('image')
    type = os.path.splitext(file.filename)[1].split('.')[1]
    if file and type in ALLOWED_EXTS:
        filename = file.filename
        content_type = file.content_type
        secure_name = secure_filename(filename)
        path = os.path.join(upload_folder, secure_name)
        file.save(path)
        data = {'profile_photo': secure_name}
        for key, val in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(obj, key, val)
        obj.save()
        redis_client.set(user_id, str(obj.to_dict()))
        return (jsonify({'status': 'Image updated successfully'}), 200)
    else:
        return jsonify({'status': 'file tyep not allowed'})


@app_views.route('/users/<string:user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a User object"""
    obj = storage.get(User, user_id)
    if not obj:
        abort(404)
    obj.delete()
    storage.save()
    return ({}, 200)

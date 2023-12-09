#!/usr/bin/python3
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import models
from models import storage
from models.user import User
from models.post import Post
import uuid

app = Flask(__name__)
socketio = SocketIO(app)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

@app.route('/', strict_slashes=False)
def chat():
    users = storage.all(User).values()
    users = sorted(users, key=lambda k:k.updated_at)

    return render_template('landing.html', cache_id=uuid.uuid4())


@app.route('/register', strict_slashes=False)
def register_user():
    return render_template('register.html', cache_id=uuid.uuid4())


@app.route('/login', strict_slashes=False)
def login():
    return render_template('login.html', cache_id=uuid.uuid4())



@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcats=True)


if __name__ == "__main__":
    socketio.run(app)

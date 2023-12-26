from flask_socketio import SocketIO
from flask import current_app

socketio = SocketIO(current_app)


@socketio.on('sendMessage', namespace='/home')
def send_message(data):
    """send message"""
    with current_app.app_context():
        print(data)
        socketio.emit('receivedMessage', data)

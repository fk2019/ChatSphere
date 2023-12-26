from flask import Flask
from .views.main import main
from .views.auth import auth
from .views.auth2 import auth2
import os
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit
from datetime import datetime

load_dotenv()

app = Flask(__name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
app.config.from_envvar('WEBDYNAMIC_SETTINGS')


app.register_blueprint(main)
app.register_blueprint(auth2)

socketio = SocketIO(app, cors_allowed_origins="https://techinspire.tech")

@app.after_request
def set_headers(response):
    response.headers['Referrer-Policy'] = 'no-referrer'
    return response

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('sendMessage')
def send_message(message):
    emit('receivedMessage', message, broadcast=True)


@socketio.on('sendFile')
def send_message(message):
    emit('receivedFile', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, port=5005, debug=True)

#!/usr/bin/python3
"""api module that registeres app_views blueprint
   and handle teardown_appcontext
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_mail import Mail
from models import storage
from os import getenv

app = Flask(__name__)
app.config.from_envvar('CHATAPI_SETTINGS')
app.mail = Mail(app)
app.register_blueprint(app_views)
cors = CORS(app, resources={r'/v1/*': {'origins': '*'}})


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return jsonified error"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv('CHAT_API_HOST', '0.0.0.0')
    port = int(getenv('CHAT_API_PORT', 5000))

    app.run(debug=True, host=host, port=port, threaded=True)

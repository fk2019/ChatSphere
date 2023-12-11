from flask import Flask
from .views.main import main
from .views.auth import auth
from .views.auth2 import auth2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
app.config.from_envvar('WEBDYNAMIC_SETTINGS')


app.register_blueprint(main)
app.register_blueprint(auth2)



@app.after_request
def set_headers(response):
    response.headers['Referrer-Policy'] = 'no-referrer'
    return response


if __name__ == '__main__':
    app.run(port=5005)

from flask import Flask
from .views.main import main
from .views.auth import auth
from .views.auth2 import auth2
import os


app = Flask(__name__)

#app.config['SECRET_KEY'] = 'secretghgfhjgfh'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
app.config['SECRET_KEY'] = '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'
app.config["SESSION_TYPE"] = "filesystem"


app.register_blueprint(main)
#app.register_blueprint(auth)
app.register_blueprint(auth2)



@app.after_request
def set_headers(response):
    response.headers['Referrer-Policy'] = 'no-referrer'
    return response


if __name__ == '__main__':
    app.run()

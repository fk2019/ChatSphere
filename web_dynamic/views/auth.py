#!/usr/bin/python3
"""auth blueprint"""
from flask import Blueprint, render_template, request, redirect, flash, url_for, session, abort
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models import storage
import os
import pathlib

GOOGLE_CLIENT_ID = "239785008997-cvo4q3efusm4al8ag0hkav4dc47g7m56.apps.googleusercontent.com"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/register_user_post"
)



auth = Blueprint('auth', __name__)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper






@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST', 'GET'])
def login_post():
    # OAuth log

    # password login
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = storage._DBStorage__session.query(User).filter_by(user_name=username).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return 'Error'
#    login_user(user)
    flash('Login successful', 'success')
    return redirect(url_for('main.profile'))


@auth.route('/register')
def register_user():
    return render_template('register.html')


@auth.route('/register_user_post', methods=['GET', 'POST'])
def register_user_post():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return session['name']

  


@auth.route('/logout')
def logout():
    return render_template('logout.html')


"""
  email = request.form.get('email')
    password = request.form.get('password')
    password = generate_password_hash(password, method='sha256')
    user_name = request.form.get('user_name')
    args = {'email': email, 'password': password, 'user_name': user_name}
    us2 = storage._DBStorage__session.query(User).filter_by(
        email=email).first()
    print(us2)
#    if us2:
 #       flash('Email already exists!')
  #      return render_template('register.html')
    user = User(**args)
    user.save()
    return redirect(url_for('auth.login'))
"""

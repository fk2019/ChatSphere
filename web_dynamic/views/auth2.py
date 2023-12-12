import os
import pathlib
import requests
from flask import Blueprint, render_template, request, redirect, flash, url_for, session, abort, current_app
import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from models.user import User
from models import storage
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

auth2 = Blueprint('auth2', __name__)



GOOGLE_CLIENT_ID = "239785008997-cvo4q3efusm4al8ag0hkav4dc47g7m56.apps.googleusercontent.com"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")


flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="https://techinspire.tech/callback"
)


def login_required(fun):
    """login_required wrapper function"""
    @wraps(fun)
    def fnc(*args, **kwargs):
        """decorated function"""
        if 'name' not in session:
            return redirect(url_for('auth2.login'))
        return fun(*args, **kwargs)
    return fnc

@auth2.route('/login')
def login():
    return render_template('login.html')


@auth2.route("/login/google")
def google_login():
    """Initiate google login. flow.authorization_url retuns a tuple of url and state"""
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@auth2.route("/login/basic", methods=['POST'])
def basic_login():
    """Initiate basic login."""
    email = request.form.get('email')
    password = request.form.get('password')
    user = storage._DBStorage__session.query(User).filter_by(
        email=email).first()
    if user and check_password_hash(user.password, password):
        session['name'] = user.user_name
        return redirect(url_for('auth2.protected_area'))
    flash('Please try again')
    return redirect(url_for('auth2.login'))


@auth2.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    #if not session["state"] == request.args["state"]:
    #   print('errrrors', session["state"], request.args["state"])
    #  abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    # verify google_id_token token
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    name = id_info.get("name")
    email = id_info.get('email')
    oauth_user_id = id_info.get('sub')
    user = storage._DBStorage__session.query(User).filter_by(
        email=email).first()
    if user:
        return redirect(url_for('auth2.protected_area'))
    kwargs = {'user_name': name, 'email': email, 'oauth_provider': 'google', 'oauth_user_id': oauth_user_id}
    requests.post('https://techinspire.tech/api/v1/users', json=kwargs)
    send_email(email, name)
    return redirect(url_for('auth2.google_login'))


def send_confirmation_email(user_email, token, name):
    """Send confirmation email"""
    mail = Mail(current_app)
    with current_app.app_context():
        msg = Message('Confirm Your Email', recipients=[user_email])
        confirmation_url = url_for('auth2.confirm_email', token=token, _external=True)
        msg.html = render_template('email_confirm.html', name=name, confirmation_url=confirmation_url)
        mail.send(msg)


def send_email(user_email, name):
    """send email"""
    mail = Mail(current_app)
    with current_app.app_context():
        msg = Message('Welcome to ChatSphere', recipients=[user_email])
        msg.html = render_template('welcome.html', name=name)
        mail.send(msg)


@auth2.route('/confirm/<string:token>')
def confirm_email(token):
    flash('Email confirmed successfully!')
    return redirect(url_for('auth2.login'))


@auth2.route('/register')
def register():
    return render_template('register.html')


@auth2.route('/register', methods=['POST'])
def register_user_post():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password = generate_password_hash(password, method='pbkdf2:sha256')
    user = storage._DBStorage__session.query(User).filter_by(
        email=email).first()
    if user:
        flash('Please try again')
        return redirect(url_for('auth2.register_user_post'))
    kwargs = {'user_name': username, 'email': email, 'password': password}
    token_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = token_serializer.dumps(email)
    send_confirmation_email(email, token, username)
    flash('Confirmation email sent to your inbox. Please confirm')
    requests.post('https://techinspire.tech/api/v1/users', json=kwargs)
    send_email(email, username)
    return render_template('confirm.html')


@auth2.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@auth2.route("/home")
@login_required
def protected_area():
    return render_template('home.html')

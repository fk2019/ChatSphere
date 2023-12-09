#!/usr/bin/python3
"""auth blueprint"""
from flask import Flask, redirect, url_for, session, request
from google_auth_oauthlib.flow import Flow
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Remove in production

# Set up OAuth 2.0 flow for Google
flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['openid', 'profile', 'email'],
    redirect_uri='http://localhost:5000/callback'
)
s = ''
# Define login route
@app.route('/login')
def login():
    authorization_url, state = flow.authorization_url(prompt='consent')
    session['state'] = state
    s = session['state']
    print(session['state'])
    return redirect(authorization_url)

# Define callback route
@app.route('/callback')
def callback():
    state = s
    print(state)
    flow.fetch_token(authorization_response=request.url, state=state)
    userinfo = flow.google_auth._userinfo(requests.get('https://www.googleapis.com/oauth2/v1/userinfo').json())
    return 'Login successful!'

# Define logout route
@app.route('/logout')
def logout():
    session.pop('oauth_state', None)
    return 'Logged out'

if __name__ == '__main__':
    app.run(debug=True)

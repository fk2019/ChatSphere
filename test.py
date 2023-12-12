#!/usr/bin/python3
"""send sample email"""
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail_config = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME': 'francisk.consult@gmail.com',
    'MAIL_PASSWORD': 'nzkd vxex dryw qzyo',
'MAIL_DEFAULT_SENDER': 'francisk.consult@gmail.com'
}
app.config.update(mail_config)
mail = Mail(app)

if __name__ =="__main__":
    with app.app_context():
        msg = Message('Hi', recipients=['fkmuiruri8@gmail.com'])
        msg.body = 'testing'
        msg.html = '<b>Testing smtp</b>'
        mail.send(msg)

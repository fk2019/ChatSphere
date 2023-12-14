#!/usr/bin/python3
"""Xmas main app"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/xmas_countdown')
def home():
    """Home route"""
    return render_template('xmas.html')


if __name__ == "__main__":
    app.run()

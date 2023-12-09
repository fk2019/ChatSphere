#!/usr/bin/python3
"""Main blueprint"""
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('landing.html')


@main.route('/profile')
def profile():
    return render_template('home.html')

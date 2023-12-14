#!/usr/bin/python3
"""Main blueprint"""
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Landing page route"""
    return render_template('landing.html')


@main.route('/xmas_countdown')
def xmas():
    """Xmas countdown route"""
    return render_template('xmas.html')

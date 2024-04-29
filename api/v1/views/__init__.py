#!/usr/bin/python3
'''Python Interpreter'''

from flask import Blueprint
'''Module to implement the Blueprint.'''


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *

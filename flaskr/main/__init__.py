# /home/yokeshwaran/Desktop/flask/flaskr/main/__init__.py
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/main')  # 'main' blueprint with '/home' prefix

from . import routes

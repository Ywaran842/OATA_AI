# /home/yokeshwaran/Desktop/flask/flaskr/main/__init__.py
from flask import Blueprint

bp = Blueprint('chat', __name__, url_prefix='/chat')  # 'main' blueprint with '/home' prefix

from . import routes

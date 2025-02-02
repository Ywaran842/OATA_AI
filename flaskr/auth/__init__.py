# /home/yokeshwaran/Desktop/flask/flaskr/auth/__init__.py
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')  # 'auth' blueprint with '/auth' prefix

from . import routes  # Import routes to register them with the blueprint

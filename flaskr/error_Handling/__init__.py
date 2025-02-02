from flask import Blueprint

bp = Blueprint('error_handling', __name__)

from . import routes
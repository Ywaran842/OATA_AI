from flask import render_template, request
from . import bp
from flaskr.auth.routes import login_required

@bp.route('/home', methods=['GET'])
@login_required
def index():
    return render_template('home.html')
from flask import render_template, url_for, redirect
from . import bp
from flask_wtf.csrf import CSRFError

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('error_handler.html'), 404

@bp.app_errorhandler(CSRFError)
def handle_csrf_error(e):
    return redirect(url_for('main.index'))  # Redirect to the sign-in page
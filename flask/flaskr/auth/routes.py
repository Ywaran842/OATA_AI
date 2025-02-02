# /home/yokeshwaran/Desktop/flask/flaskr/auth/routes.py
from flask import Blueprint, redirect, url_for, flash, request, render_template, current_app, g
from flaskr.Class.authentication import Authentication
from . import bp  # Import bp from __init__.py
from flaskr.Class.usersession import sessionAuth
from flaskr.Class.Session import SessionManager
from flaskr.wtf_Class.wtf_Auth import Loginform, Registerform
from flaskr.Email_smtp.auth_mail import mail
import threading
from functools import wraps


@bp.route('/authentication', methods=['POST'])
def signin():
    # username = request.form.get('username')
    # password = request.form.get('password')

    # if not username or not password:
    #     flash('Please enter valid credentials')
    #     return 'not login'
    formlogin = Loginform()
    #form auth
    if not formlogin.validate_on_submit():
        current_app.logger.error(f"User failed to login {formlogin.username.data}")
        return redirect(url_for('auth.render_sign_in'))
    auth = Authentication()

    #login auth
    login_result = auth.login(formlogin.username.data, formlogin.password.data)
    if login_result[0] is not None:
        login_error = SessionManager.get_session('login_error')

        #initialize the session (or) update the Session
        if login_error is None:
            login_error = 1
        else:
            login_error += 1

        SessionManager.set_session('login_error', login_error)
        #send the mail using mail.mail()
        if login_error == 3:
            ###send the mail async
            mail_thread = threading.Thread(
            target=mail.mail,
            args=('DDOS on Login page', f'{request.remote_addr} / {formlogin.username.data} ddos your site')
            )       
            mail_thread.start() 

        flash(login_result[0])
        return redirect(url_for('auth.render_sign_in'))
    else:
        token = sessionAuth.authentication(formlogin.username.data)
        #Set the Session Token
        current_app.logger.info(f"User login from IP: {request.remote_addr}")
        SessionManager.set_session('token', str(token))
        SessionManager.set_session('userid', str(login_result[1]))
        
        #Assign g variable
        return redirect(url_for('main.index'))

@bp.route('/register/update', methods=['POST'])
def register():
    error = None
    registerform = Registerform()
    if not registerform.validate_on_submit():
        flash('password must same')
        return redirect(url_for('auth.render_register'))
    # username = request.form['username']
    # password = request.form['password']
    # mailid = request.form['email']
    # mailid = 'ywaran842@gmail.com'
    # if (username is None or password is None or mailid is None):
    #     error = 'Please enter valid credentials'
    #     return redirect(url_for('auth.render_register'))
    auth = Authentication()
    register_result = auth.register(registerform.username.data, registerform.password.data, registerform.emailid.data)
    if register_result is not True:
        flash(register_result)
        return redirect(url_for('auth.render_register'))
    else:
        return redirect(url_for('auth.render_sign_in'))
        
      

@bp.route('/')  # Corrected path for '/auth/' as the default path for sign-in
def render_sign_in():
    form = Loginform()
    return render_template('sign_in.html', form=form)

@bp.route('/register')
def render_register():
    form = Registerform()
    return render_template('register.html', form=form)

def login_required(func):
    @wraps(func)  # This ensures that the wrapped function retains its original attributes
    def wrapper(*args, **kwargs):
        token = SessionManager.get_session('token')
        if token is None:
            return redirect(url_for('auth.render_sign_in'))
        if sessionAuth.Authorise(token) is None:
            return redirect(url_for('auth.render_sign_in'))
        return func(*args, **kwargs)
    return wrapper
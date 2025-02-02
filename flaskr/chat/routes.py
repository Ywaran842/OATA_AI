# /home/yokeshwaran/Desktop/flask/flaskr/main/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, g, flash, current_app, abort, jsonify
from . import bp
from flaskr.Class.Session import SessionManager
from flaskr.auth.routes import login_required
from flaskr.Class.beforequest import gset
from flaskr.Class.chat import genimichat
from flaskr.Class.getConnection import Database




@bp.before_request
def before_request():
    userid = SessionManager.get_session('userid')
    g.userid = userid

@bp.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        message = request.form['message']
        chat = genimichat.responce_with_text(message, user.id)
        if chat is None:
            return render_template('man.html')
        connection = Database.getConnection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO chat (user_id, user_chat, ai_chat) VALUES (%s, %s, %s)', (g.userid, message, chat))
        return jsonify(chat)
    else:
        return render_template('man.html')
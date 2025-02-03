# /home/yokeshwaran/Desktop/flask/flaskr/main/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, g, flash, current_app, abort, jsonify
from . import bp
from flaskr.Class.Session import SessionManager
from flaskr.auth.routes import login_required
from flaskr.Class.beforequest import gset
from flaskr.Class.chat import genimichat
from flaskr.Class.getConnection import Database
from flaskr import csrf



@bp.before_request
def before_request():
    userid = SessionManager.get_session('userid')
    g.userid = userid


@bp.route('/chatting', methods=['GET', 'POST'])
@login_required
@csrf.exempt
def chat():
    if request.method == 'POST':
        print("Received POST request")  # Debugging

        message = request.form.get('message', '').strip()
        if not message:
            print("No message received")  # Debugging
            return jsonify({'error': 'Message is required'}), 400  # Proper error

        chat = genimichat.responce_with_text(message, g.userid)
        if chat is None:
            print("AI returned None")  # Debugging
            return jsonify({'error': 'No response from AI'}), 200

        # Save to DB
        connection = Database.getConnection()
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO chat (user_id, user_chat, ai_chat) VALUES (%s, %s, %s)',
            (g.userid, message, chat)
        )
        connection.commit()
        print("Chat saved successfully")  # Debugging

        return jsonify({'response': chat})  # Expected JSON response

    return jsonify({'error': 'yokesh Invalid request method'}), 405
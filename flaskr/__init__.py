# /home/yokeshwaran/Desktop/flask/flaskr/__init__.py
import os
from flask import Flask, request_finished
from config import Config
from flask_wtf.csrf import CSRFProtect
import logging
from flaskr.Flaskrlogging import LoggerConfig
from flaskr.Class.getConnection import Database

# CSRF Protection
csrf = CSRFProtect()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DEBUG'] = True 
    app.config.from_object(Config)
    
    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping(test_config)

    # Configure logging
    logs_folder = 'logs'
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    # file_handler = logging.FileHandler(os.path.join(logs_folder, 'info.log'))
    # file_handler.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # file_handler.setFormatter(formatter)
    # app.logger.addHandler(file_handler)

    ###TO DATABASE INIT_APP###
    Database.init_app(app)
    @request_finished.connect
    def on_request_finished(sender, **extra):
        print("Request finished!")

    # # Set the logger level to INFO to capture info and higher level logs
    # app.logger.setLevel(logging.INFO)
    logging_config = LoggerConfig(app)

    # CSRF Initialization
    csrf.init_app(app)
    
    # Register Blueprints
    from .auth import bp as auth_bp
    from .main import bp as main_bp
    from .error_Handling import bp as error_bp
    from .chat import bp as chat_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(chat_bp)

    @app.errorhandler(Exception)
    def handle_error(e):
        print(f"An error occurred: {str(e)}")
        return f"An error occurred, please check the logs for details.{str(e)}", 500
    return app  

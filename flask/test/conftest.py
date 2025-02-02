import os 
import tempfile
import pytest
from flaskr import create_app
from flaskr.Class.getConnection import Database
import pymysql

with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    config = {
        'Testing': True,
        'MYSQL_HOST': 'localhost',
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': 'yokesh',
        'MYSQL_DB': 'test',
        'MYSQL_PORT': 3306
    }

    app = create_app(config)
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SECRET_KEY'] = 'supersecretkey'
    with app.app_context():
        cursor = Database.getConnection().cursor()
        cursor.execute('USE test')
        cursor.execute(_data_sql)

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthAction(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='waran123', password='waran123'):
        return self._client.post(
            '/auth/authentication',
            data={'username': username, 'password': password}
        )

@pytest.fixture
def auth(client):
    return AuthAction(client)





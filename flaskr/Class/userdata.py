from .getConnection import Database
from flaskr.error.writeerror import write_error_to_file
from uuid import uuid4
from datetime import datetime
import base64

class userdata:
    def __init__(self, username):
        self.username = username
        self.id = None
        self.connection = Database.getConnection()
        if self.connection is None:
            write_error_to_file('Error connecting to database constructor', 'usersession')
            raise Exception('Error connecting to database constructor')
        sql = 'SELECT id FROM Users WHERE username = %s OR id = %s'
        cursor = self.connection.cursor()
        cursor.execute(sql, (self.username, self.username))
        self.user = cursor.fetchone()
        self.id = self.user['id']
        if self.user is None:
            write_error_to_file('Invalid credentials', 'usersession')

            

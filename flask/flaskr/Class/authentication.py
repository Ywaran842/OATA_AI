from .getConnection import Database
from flaskr.error.writeerror import write_error_to_file
from werkzeug.security import check_password_hash, generate_password_hash
import uuid 

class Authentication: 
    def __init__(self):
        self.connection = Database.getConnection()
        if self.connection is None:
            write_error_to_file('Error connecting to database constructor', 'Authentication')
            raise Exception('Error connecting to database constructor')
        
    @staticmethod
    def login(username, password):
        error = None
        connection = Database.getConnection()
        if connection is None:
            raise Exception('Error connecting to database login')
        cursor = connection.cursor()
        sql = 'SELECT * FROM Users WHERE USERNAME = %s'  
        cursor.execute(sql, (username,))
        user = cursor.fetchone()  # Fetch the first result of the query

        if user is None:
            error = 'Invalid credentials'
            return error, None
        elif not check_password_hash(user['password'], password):  # Compare password hash
            error = 'Invalid password'
            return error, None
        else:
            return None, user['id']

    @staticmethod
    def register(username, password, mailid):
        error = None
        connection = Database.getConnection()
        if connection is None:
            raise Exception('Error connecting to database register')
        cursor = connection.cursor()
        sql = 'SELECT username FROM Users WHERE username = %s'
        cursor.execute(sql, (username,))
        user = cursor.fetchone()  # Fetch the result to check if the user already exists

        if user is not None:
            error = 'Username already exists'
            return error
        else:
            hashed_password = generate_password_hash(password)  # Hash the password before storing
            uuid_id = uuid.uuid4()
            sql = 'INSERT INTO Users (username, password, mailid, id) VALUES (%s, %s, %s, %s)'
            cursor.execute(sql, (username, hashed_password, mailid, uuid_id))
            connection.commit()
            return True
        

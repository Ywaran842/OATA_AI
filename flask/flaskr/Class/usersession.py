from flaskr.Class.userdata import userdata
from flask import request
from hashlib import md5
from random import randint
from .getConnection import Database
from datetime import datetime
import uuid
from .Session import SessionManager
from flaskr.error.writeerror import write_error_to_file

class sessionAuth:

    @staticmethod
    def authentication(username):
        if username is None:
            return None
        connection = Database.getConnection()
        #user instance to get theuser id
        id = uuid.uuid4()
        useruid = userdata(username)
        ip = request.remote_addr
        useragent = request.user_agent.string
        token = md5((str(randint(0,1000))+ip+useragent).encode('utf-8')).hexdigest()
        login_time = datetime.now()
        sql = 'INSERT INTO session (id, uid, token, login_time, ip, user_agent) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor = connection.cursor()
        cursor.execute(sql, (id, useruid.id, token, login_time, ip, useragent))
        connection.commit()
        return token


    @staticmethod
    def Authorise(token):
        data = sessionAuth(token)
        if(data.isvalid() is None):
            return None
        if((request.remote_addr == data.get_ip()) and (request.user_agent.string == data.get_user_agent())):
            return True
        else:
            return None
            

    @staticmethod
    def logout(token):
        connection = Database.getConnection()
        sql = 'DELETE FROM session WHERE token = %s'
        cursor = connection.cursor()
        cursor.execute(sql, token)
        connection.commit()
        cursor.close()
        connection.close()
        

    def __init__(self, token):
        self.connection = Database.getConnection()
        if self.connection is None:
            write_error_to_file('Error connecting to database constructor', 'usersession')
            raise Exception('Error connecting to database constructor')
        self.token = token
        sql = 'SELECT * FROM session WHERE token = %s'
        cursor = self.connection.cursor()
        cursor.execute(sql, (self.token))
        self.data = cursor.fetchone()

    def isvalid(self):
        if self.data is None:
            return False
        return True

    def get_ip(self):
        return self.data['ip']

    def get_user_agent(self):
        return self.data['user_agent']

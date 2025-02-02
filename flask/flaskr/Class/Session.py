from flask import session

class SessionManager:
    #set session
    @staticmethod
    def set_session(key, value):
        session[key] = value
    #get session
    @staticmethod
    def get_session(key):
        if key not in session:
            return None
        return session[key]
    #delete session
    @staticmethod
    def delete_session(key):
        if key not in session:
            return None
        del session[key]
    #clear session
    def clear_session():
        session.clear()

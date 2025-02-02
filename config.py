import os

class Config:
    DEFAULT_LANGUAGE = 'en'
    WTF_CSRF_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE']
    WTF_CSRF_TIMR_LIMIT = 360
    MYSQL_PORT = 3306
    MYSQL_DB = 'yokesh'
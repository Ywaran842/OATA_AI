import pymysql
from pymysql.cursors import DictCursor
from flaskr.error.writeerror import write_error_to_file
from flask import g, current_app
import click

class Database:
    @staticmethod
    def getConnection():
        if 'db' not in g:
            try:
                g.db = pymysql.connect(
                    host=current_app.config['MYSQL_HOST'],
                    user=current_app.config['MYSQL_USER'],
                    password=current_app.config['MYSQL_PASSWORD'],
                    database=current_app.config['MYSQL_DB'],
                    port=current_app.config['MYSQL_PORT'],
                    cursorclass=DictCursor
                )
                return g.db
            except pymysql.MySQLError as e:
                write_error_to_file(str(e)+' getconnection', 'Database')
                print(str(e))
                return None
        else:
            return g.db
    
    @staticmethod
    def close_db(e=None):
        db = g.pop('db',None)
        if db is not None:
            db.close()

    @staticmethod
    def init_db():
        db = Database.getConnection()
        with current_app.open_resource('schema/schema.sql') as f:
            sql_script = f.read().decode('utf8')
            cursor = db.cursor()
            cursor.execute(sql_script)
            db.commit()

    @staticmethod
    @click.command('init_db')
    def init_command():
        Database.init_db()
        click.echo('Initialise the database')

    @staticmethod
    def init_app(app):
        app.teardown_appcontext(Database.close_db)
        app.cli.add_command(Database.init_command)





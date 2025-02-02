from flaskr.Class.getConnection import Database

def gset(token):
    connection = Database.getConnection()
    sql = 'SELECT u.id from users as u join session as s on u.id = s.uid where s.token = %s'
    cursor = connection.cursor()
    cursor.execute(sql, (token))
    result = cursor.fetchone()
    return result


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

    def get_post(self): 
        sql = 'SELECT p.likes, p.id, p.title, p.body, p.created, p.img , p.uid, a.username from posts as p join Users as a on p.uid = a.id ORDER BY p.created DESC'
        cursor = self.connection.cursor()
        cursor.execute(sql)
        posts = cursor.fetchall()
        if posts is None:
            return None
        fromat_post = []
        for post in posts:
            img_data = post['img']
            if img_data:
                img_bas64 = base64.b64encode(img_data).decode('utf-8')
                post['img'] = f"data:image/png;base64,{img_bas64}"
            else:
                post['img'] = None
            fromat_post.append(post)
        return fromat_post    
    
    def set_post(self, title, body, img):
        uuid_id = uuid4()
        sql = 'Insert into posts (id, title, body, img, uid, created) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor = self.connection.cursor()
        cursor.execute(sql, (uuid_id, title, body, img, self.id, datetime.now()))
        self.connection.commit()

    def update_post(self, title, body, img, id):
        sql = 'UPDATE posts SET title = %s, body = %s, img = %s WHERE id = %s'
        cursor = self.connection.cursor()
        cursor.execute(sql, (title, body, img, id))
        posts = cursor.fetchone()

        if posts is None:
            return None
        if posts['uid'] != self.id:
            return None
        return True
    
    def Deletepost(self, id):
        sql = 'DELETE FROM posts WHERE id = %s'
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, (id,))  # Ensure (id,) is a tuple
            self.connection.commit()   # Commit using the connection object
            if cursor.rowcount == 0:   # No rows affected
                return False
            return True
        except Exception as e:
            self.connection.rollback()  # Rollback in case of an error
            return False
        finally:
            cursor.close()  # Always close the cursor

    
    def Like(self, id):
        sql = 'UPDATE posts SET likes = likes + 1 WHERE id = %s'
        cursor = self.connection.cursor()
        cursor.execute(sql, (id))
        cursor.commit()
        if cursor.rowcount == 0:
            return False
        return True
    
    def Get_post_by_id(self, id):
        sql = 'SELECT p.id, title, body, p.img , p.uid, a.id from posts as p join Users as a on p.uid = a.id WHERE p.id = %s'
        cursor = self.connection.cursor()
        cursor.execute(sql, (id))
        post = cursor.fetchone()
        if post is None:
            return None
        img_data = post['img']
        if img_data:
            img_base64 = base64.b64encode(img_data).decode('utf-8')
            post['img'] = f"data:image/png;base64,{img_base64}"
        else:
            post['img'] = None
        return post
            

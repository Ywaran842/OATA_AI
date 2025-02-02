import pymysql
import unittest

# Assuming your Config class is in a separate file, import it
# from config import Config

class Config:
    MYSQL_HOST = 'localhost'  # Use 'localhost' if testing on local machine
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'yokesh'
    MYSQL_DB = 'yokesh'
    MYSQL_PORT = 3306


class TestDatabaseConnection(unittest.TestCase):
    def test_mysql_connection(self):
        """Test if the MySQL connection can be established with given Config settings."""
        try:
            connection = pymysql.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DB,
                port=Config.MYSQL_PORT
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * from Users")
            version = cursor.fetchone()
            print(f"MySQL version: {version}")
            self.assertIsNotNone(version)  # Check that the version is not None
        except pymysql.MySQLError as e:
            self.fail(f"MySQL connection test failed: {e}")
        finally:
            if connection:
                connection.close()

if __name__ == '__main__':
    unittest.main()

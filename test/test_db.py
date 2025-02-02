import pytest
import pymysql
from flaskr.Class.getConnection import Database

def test_get_db_closed(app):
    # Open a database connection
    with app.app_context():
        db = Database.getConnection()
        assert db is Database.getConnection()  # Ensure that we are getting the connection correctly
    

    # Try to use the closed connection and expect an exception
    with app.app_context():  # Ensure you're within the app context
        with pytest.raises(pymysql.MySQLError) as e:  # Expect a MySQLError for pymysql
            try:
                db.ping(reconnect=False)  # This should raise an error because db is closed
            except pymysql.MySQLError as ex:
                print(f"Caught exception: {str(ex)}")
                raise ex  # Reraise the exception to catch it in pytest

        # Now check the exception message for connection closure
        assert 'closed' in str(e.value) or 'not connected' in str(e.value)

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False
    
    def fake_init_db():
        Recorder.called =True

    monkeypatch.setattr('flaskr.Class.getConnection.Database.init_db', fake_init_db)
    result = runner.invoke(args=['init_db'])
    assert 'Initialise' in result.output
    assert Recorder.called
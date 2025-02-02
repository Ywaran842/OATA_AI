import pytest
from flaskr.Class.getConnection import Database

def test_reister(client, app):
    # assert client.get('/auth/register').status_code == 200
    # response = client.post(
    #     '/auth/register/update', data={'username': 'waran123', 'password': 'waran123', 'confirmpassword': 'waran123','emailid': 'waran@gmail.com'}
    # )
    # assert response.headers['Location'] == '/auth/'

    with app.app_context():
        cursor = Database.getConnection().cursor()
        cursor.execute("select * from Users where username = 'waran123'")
        result = cursor.fetchone()
        assert result is not None
        
def test_login(client, auth):
    assert client.get('/auth/').status_code == 200
    response = auth.login()
    assert response.headers['Location'] == '/home/'

@pytest.mark.parametrize(('username', 'password', 'message'), ( 
    ('a', 'yokesh', b'Sign in'),
    ('yokesh', 'a', b'Sign in')
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    if response.status_code == 302:
        response = auth._client.get(response.headers['Location']) 
    assert message in response.data


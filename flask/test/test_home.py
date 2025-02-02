import pytest
from flaskr.Class.getConnection import Database

def test_index(client, auth):
    response = client.get('/home')
    
    # Follow multiple redirects if needed
    while response.status_code in [302, 308]:
        response = client.get(response.headers['Location'])
    
    # Debugging: print response data and status code
    print(response.data)
    print(response.status_code)
    
    assert b'Sign in' in response.data

    assert b"Register" in response.data

    auth.login()
    response = client.get('/home')
    while response.status_code in [302, 308]:
        response = client.get(response.headers['Location'])
    assert b'Create' in response.data

@pytest.mark.parametrize('path', (
    'home/create',
    'home/1/update',
    'home/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/"

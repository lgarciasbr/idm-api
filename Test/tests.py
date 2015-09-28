import unittest
from app import app


class Test_um(unittest.TestCase):

    def setUp(self):
        self.app = app

    def login(self, username, password):
        return self.app.post('/login', data={'username': username, 'password': password}, follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data

        rv = self.logout()
        assert 'You were logged out' in rv.data

        rv = self.login('adminx', 'default')
        assert 'Invalid username or password' in rv.data

        rv = self.login('admin', 'defaultx')
        assert 'Invalid username or password' in rv.data

if __name__ == '__main__':
    unittest.main()

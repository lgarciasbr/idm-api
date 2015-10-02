import json
import unittest

from Account.main_app import app
from config import PROJECT_NAME, PROJECT_DESCRIPTION, MSN_404, MSG_LOGIN, MSG_LOGOUT, MSG_LOGIN_ERROR, MSG_INVALID_TOKEN


class TestSolution(unittest.TestCase):
    # Welcome
    def test_welcome_assert(self):
        tester = app.test_client(self)

        response = tester.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['description'], PROJECT_DESCRIPTION)
        self.assertEqual(json.loads(response.data)['project'], PROJECT_NAME)

    # Login
    def login(self, username, password):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]

        data_json = json.dumps({'username': username, 'password': password})

        json_data_length = len(data_json)
        header.append(('Content-Length', json_data_length))

        return tester.post('/login', data=data_json, headers=header)

    def test_login_assert(self):
        response = self.login('admin', 'default')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN)

    def test_login_not_assert_user(self):
        response = self.login('error', 'default')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_password(self):
        response = self.login('admin', 'error')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_username_password(self):
        response = self.login('error', 'error')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_get(self):
        tester = app.test_client(self)

        response = tester.get('/login')

        self.assertEqual(response.status_code, 405)

    def test_login_not_assert_post(self):
        tester = app.test_client(self)

        response = tester.post('/login')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    # Logout
    def logout(self, token):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]

        header.append(('token', token))

        return tester.post('/logout', headers=header)

    def test_logout_assert(self):

        response_login = self.login('admin', 'default')

        if response_login.status_code == 200:
            response = self.logout(json.loads(response_login.data)['token'])

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)['message'], MSG_LOGOUT)

    def test_logout_assert_second_shot(self):

        response_login = self.login('admin', 'default')

        token = json.loads(response_login.data)['token']

        if response_login.status_code == 200:
            # logout
            self.logout(token)
            # Second Shot
            response = self.logout(token)

            self.assertEqual(response.status_code, 403)
            self.assertEqual(json.loads(response.data)['message'], MSG_INVALID_TOKEN)
            self.assertEqual(json.loads(response.data)['token'], token)

    def test_logout_not_assert(self):
        response = self.logout('error')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_INVALID_TOKEN)
        self.assertEqual(json.loads(response.data)['token'], 'error')

    # Error
    def test_error_404_assert(self):
        tester = app.test_client(self)

        response = tester.get('/pnf')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data)['status'], 404)


if __name__ == '__main__':
    unittest.main()

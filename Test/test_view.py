import json
import unittest

from Account.view import app
from config import PROJECT_NAME, PROJECT_DESCRIPTION, MSG_LOGIN, MSG_LOGOUT, MSG_LOGIN_ERROR, MSG_INVALID_TOKEN


class test_solution(unittest.TestCase):
    # Welcome
    def test_welcome_assert(self):
        tester = app.test_client(self)

        response = tester.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['description'], PROJECT_DESCRIPTION)
        self.assertEqual(json.loads(response.data)['project'], PROJECT_NAME)


    # Login
    def login_v1(self, username, password):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]
        header.append(('ver', '1'))

        data_json = json.dumps({'username': username, 'password': password})

        return tester.post('/login', data=data_json, headers=header)

    def test_login_assert(self):
        response = self.login_v1('admin', 'default')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN)

    def test_login_not_assert_user(self):
        response = self.login_v1('error', 'default')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_password(self):
        response = self.login_v1('admin', 'error')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_username_password(self):
        response = self.login_v1('error', 'error')

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
    def logout_v1(self, token):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]
        header.append(('ver', '1'))
        header.append(('token', token))

        return tester.post('/logout', headers=header)

    def test_logout_assert(self):
        response_login = self.login_v1('admin', 'default')

        response = self.logout_v1(json.loads(response_login.data)['token'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGOUT)

    def test_logout_assert_second_shot(self):
        response_login = self.login_v1('admin', 'default')

        token = json.loads(response_login.data)['token']

        if response_login.status_code == 200:
            # logout
            self.logout_v1(token)
            # Second Shot
            response = self.logout_v1(token)

            self.assertEqual(response.status_code, 403)
            self.assertEqual(json.loads(response.data)['message'], MSG_INVALID_TOKEN)
            self.assertEqual(json.loads(response.data)['token'], token)

    def test_logout_not_assert(self):
        response = self.logout_v1('error')

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

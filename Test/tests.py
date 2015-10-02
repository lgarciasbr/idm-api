import json
import unittest

from Account.main_app import app
from config import PROJECT_NAME, PROJECT_DESCRIPTION, MSN_404, MSG_LOGIN, MSG_LOGOUT, MSG_LOGIN_ERROR


#todo arrumar os testes de logout

class TestSolution(unittest.TestCase):

    # Welcome
    def test_welcome_assert(self):
        tester = app.test_client(self)

        response = tester.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            '{\n  "Description": "' + PROJECT_DESCRIPTION + '", \n  "Project": "' + PROJECT_NAME + '"\n}'
        )


    # Login
    def test_login_assert(self):

        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]

        data_json = json.dumps({'username': 'admin', 'password': 'default'})

        json_data_length = len(data_json)
        header.append(('Content-Length', json_data_length))

        response = tester.post('/login', data=data_json, headers=header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.data)['Message'],
            MSG_LOGIN
        )

    def test_login_not_assert_user(self):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]

        data_json = json.dumps({'username': 'error', 'password': 'default'})

        json_data_length = len(data_json)
        header.append(('Content-Length', json_data_length))

        response = tester.post('/login', data=data_json, headers=header)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.data,
            MSG_LOGIN_ERROR
        )

    def test_login_not_assert_password(self):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]

        data_json = json.dumps({'username': 'admin', 'password': 'error'})

        json_data_length = len(data_json)
        header.append(('Content-Length', json_data_length))

        response = tester.post('/login', data=data_json, headers=header)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.data,
            MSG_LOGIN_ERROR
        )

    def test_login_not_assert_username_password(self):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]

        data_json = json.dumps({'username': 'error', 'password': 'error'})

        json_data_length = len(data_json)
        header.append(('Content-Length', json_data_length))

        response = tester.post('/login', data=data_json, headers=header)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.data,
            MSG_LOGIN_ERROR
        )

    def test_login_not_assert_get(self):
        tester = app.test_client(self)

        response = tester.get('/login')

        self.assertEqual(response.status_code, 405)

    def test_login_not_assert_post(self):
        tester = app.test_client(self)

        response = tester.post('/login')

        self.assertEqual(response.status_code, 403)


    # Logout
    def test_logout_assert(self):
        tester = app.test_client(self)

        response = tester.get('/logout')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            MSG_LOGOUT
        )

    def test_logout_not_assert(self):
        tester = app.test_client(self)

        response = tester.get('/logout')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(
            response.data,
            'I was logged out'
        )


    # Error
    def test_error_404_assert(self):
        tester = app.test_client(self)

        response = tester.get('/pnf')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.data,
            '{\n  "message": "' + MSN_404 + 'http://localhost/pnf", \n  "status": 404\n}'
        )


if __name__ == '__main__':
    unittest.main()

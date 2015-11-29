import json
import unittest

from lg_idm import app
from config import MSG_LOGIN, MSG_LOGOUT, MSG_LOGIN_ERROR,\
    MSG_INVALID_TOKEN, MSN_400, EMAIL_TEST, PWD_TEST


class AuthenticationSolution(unittest.TestCase):
    # Account
    # Register
    def test_account_register_assert(self):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]
        header.append(('ver', '1'))

        data_json = json.dumps({'email': EMAIL_TEST, 'password': PWD_TEST})

        response = tester.post('/account', data=data_json, headers=header)

        self.assertEqual(response.status_code, 200)


    # todo precisa fazer os testes nao passando todos os itens do header no login
    # Authentication
    # Login
    def login_v1(self, email, password):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]
        header.append(('ver', '1'))

        data_json = json.dumps({'email': email, 'password': password})

        return tester.post('/auth', data=data_json, headers=header)

    def test_login_assert(self):
        response = self.login_v1(EMAIL_TEST, PWD_TEST)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN)

    def test_login_not_assert_user(self):
        response = self.login_v1('wrong_email', PWD_TEST)

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_password(self):
        response = self.login_v1(EMAIL_TEST, 'wrong_password')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_username_password(self):
        response = self.login_v1('wrong_email', 'wrong_password')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data)['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_get(self):
        tester = app.test_client(self)

        response = tester.get('/auth')

        self.assertEqual(response.status_code, 405)

    def test_login_not_assert_post(self):
        tester = app.test_client(self)

        response = tester.post('/auth')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['message'], MSN_400)

    # todo precisa fazer os testes nao passando todos os itens do header no login
    # Logout
    def logout_v1(self, token):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]
        header.append(('ver', '1'))
        header.append(('token', token))

        return tester.delete('/auth', headers=header)

    def test_logout_assert(self):
        response_login = self.login_v1(EMAIL_TEST, PWD_TEST)

        token = json.loads(response_login.data)['token']

        if response_login.status_code == 200:
            # logout
            response = self.logout_v1(token)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)['message'], MSG_LOGOUT)

    def test_logout_assert_second_shot(self):
        response_login = self.login_v1(EMAIL_TEST, PWD_TEST)

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

    def test_logout_not_assert_no_header(self):
        tester = app.test_client(self)

        response = tester.delete('/auth')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['message'], MSN_400)

    def test_logout_not_assert_get(self):
        tester = app.test_client(self)

        response = tester.get('/auth')

        self.assertEqual(response.status_code, 405)

    # Error
    def test_error_404_assert(self):
        tester = app.test_client(self)

        response = tester.get('/pnf')

        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

import json
import time
import unittest
from idManager.settings import MSG_LOGIN, MSG_LOGOUT, MSG_LOGIN_ERROR,\
    MSG_INVALID_TOKEN, EMAIL_TEST, PWD_TEST, CHECK_EMAIL_DELIVERABILITY
from manage import app

class AuthenticationSolution(unittest.TestCase):

    def setUp(self):
        # Register an user for test purpose.
        self.register_v1(EMAIL_TEST, PWD_TEST)

    def tearDown(self):
        pass

    # def tearDown(self):
        # todo remover o usuario criado para o teste.
        # todo sera que nao devo apagar o banco criado?

    # Account
    # Register
    def register_v1(self, email, password):
        tester = app.test_client(self)

        header = {'Content-Type': 'application/json',
                  'ver': '1'}

        data_json = json.dumps({'email': email, 'password': password})

        return tester.post('/accounts/', data=data_json, headers=header)


    # todo precisa fazer os testes nao passando todos os itens do header no login
    # todo precisa fazer os testes nao passando o login e depois a senha e os dois.
    # Authentication
    # Login
    def login_v1(self, email, password):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]
        header.append(('ver', '1'))

        data_json = json.dumps({'email': email, 'password': password})

        return tester.post('/auth/', data=data_json, headers=header)

    def test_login_assert(self):
        response = self.login_v1(EMAIL_TEST, PWD_TEST)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['message'], MSG_LOGIN)

    def test_login_not_assert_user(self):
        response = self.login_v1('wrong_email', PWD_TEST)

        self.assertEqual(response.status_code, 400)

    def test_login_not_assert_password(self):
        response = self.login_v1(EMAIL_TEST, 'wrong_password')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['message'], MSG_LOGIN_ERROR)

    def test_login_not_assert_username_password(self):
        response = self.login_v1('wrong_email', 'wrong_password')

        self.assertEqual(response.status_code, 400)

    def test_login_not_assert_get(self):
        tester = app.test_client(self)

        response = tester.get('/auth/')

        self.assertEqual(response.status_code, 400)

    def test_login_not_assert_post(self):
        tester = app.test_client(self)

        response = tester.post('/auth/')

        self.assertEqual(response.status_code, 400)
        # self.assertEqual(json.loads(response.data.decode('utf-8'))['message'], MSN_400)

    # todo precisa fazer os testes nao passando todos os itens do header no login
    # Logout
    def logout_v1(self, token):
        tester = app.test_client(self)

        header = [('Content-Type', 'application/json')]
        header.append(('ver', '1'))
        header.append(('token', token))

        return tester.delete('/auth/', headers=header)

    def test_logout_assert(self):
        response_login = self.login_v1(EMAIL_TEST, PWD_TEST)

        token = json.loads(response_login.data.decode('utf-8'))['auth']['_token']

        if response_login.status_code == 200:
            # logout
            response = self.logout_v1(token)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data.decode('utf-8'))['message'], MSG_LOGOUT)

    def test_logout_assert_second_shot(self):
        response_login = self.login_v1(EMAIL_TEST, PWD_TEST)

        token = json.loads(response_login.data.decode('utf-8'))['auth']['_token']

        if response_login.status_code == 200:
            # logout
            self.logout_v1(token)

            # Second Shot
            time.sleep(1)
            response = self.logout_v1(token)

            self.assertEqual(response.status_code, 403)
            self.assertEqual(json.loads(response.data.decode('utf-8'))['message'], MSG_INVALID_TOKEN)

    def test_logout_not_assert(self):
        response = self.logout_v1('error')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['message'], MSG_INVALID_TOKEN)

    def test_logout_not_assert_no_header(self):
        tester = app.test_client(self)

        response = tester.delete('/auth/')

        self.assertEqual(response.status_code, 400)

    def test_logout_not_assert_get(self):
        tester = app.test_client(self)

        response = tester.get('/auth/')

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()

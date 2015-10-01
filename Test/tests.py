from Account.main_app import app

import unittest
from config import PROJECT_NAME, PROJECT_DESCRIPTION

#todo criar os testes de login
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

    def test_welcome_not_assert(self):
        tester = app.test_client(self)

        response = tester.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(
            response.data,
            'Welcome!'
        )

    # Logout
    def test_logout_assert(self):
        tester = app.test_client(self)

        response = tester.get('/logout')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            'You were logged out'
        )

    def test_logout_not_assert(self):
        tester = app.test_client(self)

        response = tester.get('/logout')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(
            response.data,
            'I was logged out'
        )

    # Error 404
    def test_error_404_assert(self):
        tester = app.test_client(self)

        response = tester.get('/pnf')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.data,
            '{\n  "message": "Not Found: http://localhost/pnf", \n  "status": 404\n}'
        )

    def test_error_404_not_assert(self):
        tester = app.test_client(self)

        response = tester.get('/pnf')

        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(
            response.data,
            'Not Found'
        )


if __name__ == '__main__':
    unittest.main()

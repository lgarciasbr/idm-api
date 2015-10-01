from Account.main_app import app

import unittest
import json


class TestSolution(unittest.TestCase):

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
            '{\n  "message": "Not Found: http://127.0.0.1:5000/eux", \n  "status": 404\n}'
        )


if __name__ == '__main__':
    unittest.main()
from Account.main_app import app

import unittest
import json


class TestSolution(unittest.TestCase):


    def test_index_assert(self):

        tester = app.test_client(self)

        response = tester.get('/logout')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            'You were logged out'
        )


    def test_index_not_assert(self):

        tester = app.test_client(self)

        response = tester.get('/logout')

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(
            response.data,
            'I was logged out'
        )


if __name__ == '__main__':
    unittest.main()
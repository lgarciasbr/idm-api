from Account.main_app import app

import unittest
import json


class TestSolution(unittest.TestCase):

  def test_index(self):

    tester = app.test_client(self)

    response = tester.get('/logout')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(
        response.data,
        'You were logged out'
    )

if __name__ == '__main__':
    unittest.main()
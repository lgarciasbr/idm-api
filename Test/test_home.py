import json
import unittest

from runserver import app
from config import PROJECT_NAME, PROJECT_DESCRIPTION


class HomeSolution(unittest.TestCase):
    # Welcome
    def test_welcome_assert(self):
        tester = app.test_client(self)

        response = tester.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['description'], PROJECT_DESCRIPTION)
        self.assertEqual(json.loads(response.data)['project'], PROJECT_NAME)


if __name__ == '__main__':
    unittest.main()

import json
import unittest

from manage import app
from config import PROJECT_NAME, PROJECT_DESCRIPTION


class HomeSolution(unittest.TestCase):
    # Welcome
    def test_welcome_assert(self):
        tester = app.test_client(self)

        response = tester.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['description'], PROJECT_DESCRIPTION)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['project'], PROJECT_NAME)

    # todo Verificar se nao existem outros testes como 403 que podem ser feitos.
    # Error
    def test_error_404_assert(self):
        tester = app.test_client(self)

        response = tester.get('/pnf')

        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

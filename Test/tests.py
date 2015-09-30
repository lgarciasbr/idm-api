from Account.main_app import app
import unittest
import json

class SolutionTestCase(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def logout(self):
        tester = app.test_client(self)

        response = tester.get('/', content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            json.dumps({'a':'Hello Memcached!', 'b':'Hello JSon!', 'c':'\o/'})
        )

'''
    def test_index(self):

        tester = app.test_client(self)

        response = tester.get('/stunticons.json', content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            json.dumps([
                "Motormaster",
                "Dead End",
                "Breakdown",
                "Wildrider",
                "Drag Strip"
            ])
        )

    def login(self, data, headers):
        json_data = json.dumps(data)
        response = self.app.post('/login', data=json_data, content_type=headers)


    def test_login_logout(self):
        headers = [('Content-Type', 'application/json')]
        data = {'username': 'admin', 'password': 'default'}
        rv = self.login(data, headers)
        assert 'You were logged in' in rv.data


        rv = self.logout
        assert 'You were logged out' in rv.data

        rv = self.login('adminx', 'default')
        assert 'Invalid username or password' in rv.data

        rv = self.login('admin', 'defaultx')
        assert 'Invalid username or password' in rv.data


    def test_sum(self):
        tester = app.test_client(self)
        response = tester.get('/_add_numbers?a=2&b=6', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Check that the result sent is 8: 2+6
        self.assertEqual(json.loads(response.data), {"result": 8})


    # This test will purposely fail
    # We are checking that 2+6 is 10
    def test_sum_fail(self):
        tester = app.test_client(self)
        response = tester.get('/_add_numbers?a=2&b=6', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"result": 10})
'''

if __name__ == '__main__':
    unittest.main()
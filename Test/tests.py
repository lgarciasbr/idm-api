from Account import app
import unittest
import json

class test(unittest.TestCase):

    def setUp(self):
        pass

    def login(self, username, password):
        tester = app.test_client(self)
        return tester.post('/login', data={'username': username, 'password': password}, follow_redirects=True)

        #response = self.client.get("/ajax/")
        #self.assertEquals(response.json, dict(success=True))

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data

        rv = self.logout
        assert 'You were logged out' in rv.data

        rv = self.login('adminx', 'default')
        assert 'Invalid username or password' in rv.data

        rv = self.login('admin', 'defaultx')
        assert 'Invalid username or password' in rv.data

'''
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

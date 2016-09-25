import unittest
from Flaskblog import app
from Flaskblog.config.config import PASSWORD, USERNAME


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        """
        Creates a test client
        """
        self.app = app.test_client()

    def login(self, username, password):
        """
        Login helper function
        """
        return self.app.post('/login', data=dict(
            username=username,
            password=password),
                             follow_redirects=True)

    def logout(self):
        """
        Logout helper function
        """
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        """
        Test login and logout
        using helper functions
        """
        res_post = self.login(USERNAME, PASSWORD)
        self.assertIn(b'You were logged in', res_post.data)
        res_post = self.logout()
        self.assertIn(b'You were logged out', res_post.data)
        res_post = self.login(USERNAME + 'a', PASSWORD)
        self.assertIn(b'Invalid username or password', res_post.data)
        res_post = self.login(USERNAME, PASSWORD + '1')
        self.assertIn(b'Invalid username or password', res_post.data)

if __name__ == '__main__':
    unittest.main()

import os
import unittest
from Flaskblog import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """
        Initial test
        ensure flask was set up correctly
        """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        """
        Initial test
        ensure that the database exists
        """
        tester = os.path.exists("/tmp/Myblog.db")
        self.assertTrue(tester)

if __name__ == '__main__':
    unittest.main()

import os
import tempfile
import unittest
import Flaskblog
from Flaskblog import app
from Flaskblog.db.db import init_db


class BlogTestCase(unittest.TestCase):
    def setUp(self):
        """
        Before each test,
        set up a blank database
        """
        self.db_fd, Flaskblog.test_data = tempfile.mkstemp()
        self.app = Flaskblog.app.test_client()
        with app.app_context():
            init_db()

    def tearDown(self):
        """
        Destroy blank temp database
        after each test
        """
        os.close(self.db_fd)
        os.unlink(Flaskblog.test_data)

    def test_empty_db(self):
        res_post = self.app.get('/home')
        self.assertIn(b'No entries here so far', res_post.data)


if __name__ == '__main__':
    unittest.main()

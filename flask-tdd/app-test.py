from app import app
import unittest
import os


class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'hello, world!')

    def test_database(self):
        tester = os.path.exists('flaskr.db')
        self.assertTrue(tester)


if __name__ == '__main__':
    unittest.main()

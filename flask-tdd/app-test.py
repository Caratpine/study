from app import app, init_db
import unittest
import os
import tempfile
import json


class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        tester = os.path.exists('flaskr.db')
        self.assertTrue(tester)


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data

    def test_login_logout(self):
        rv = self.login(
            app.config['USERNAME'],
            app.config['PASSWORD']
        )
        assert b'You were logged in' in rv.data
        rv = self.logout()
        assert b'You were logged out' in rv.data
        rv = self.login(
            app.config['USERNAME'] + 'x',
            app.config['PASSWORD']
        )
        assert b'Invalid username' in rv.data
        rv = self.login(
            app.config['USERNAME'],
            app.config['PASSWORD'] + 'x'
        )
        assert b'Invalid password' in rv.data

    def test_messages(self):
        self.login(
            app.config['USERNAME'],
            app.config['PASSWORD']
        )
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert b'No entries here so far' not in rv.data
        assert b'&lt;Hello&gt;' in rv.data
        assert b'<strong>HTML</strong> allowed here' in rv.data

    def test_delete_message(self):
        rv = self.app.get('/delete/1')
        data = json.loads((rv.data).decode('utf-8'))
        self.assertEqual(data['status'], 1)


if __name__ == '__main__':
    unittest.main()

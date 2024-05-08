import unittest
from app import app, db, User

class FlaskTestCase(unittest.TestCase):

    # TODO: Update if needed
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()
            user1 = User(username='testuser1', password='testpass1')
            user2 = User(username='testuser2', password='testpass2')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_logout(self):
        response = self.app.post('/login', data=dict(username='testuser1', password='testpass1'), follow_redirects=True)
        assert b'Logged in as: testuser1' in response.data
        response = self.app.get('/logout', follow_redirects=True)
        assert b'Login' in response.data

    # TODO: write unit test to test route register
    # TODO: write unit test to test function load_user

if __name__ == '__main__':
    unittest.main()

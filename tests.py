from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_posts(self):
        # create four users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])

        
        now = datetime.utcnow()

        # create four posts
        p1 = Post(title="help", description="post from john", author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(title="help", description="post from susan", author=u2, timestamp=now + timedelta(seconds=4))
        p3 = Post(title="help", description="post from mary", author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(title="help", description="post from david", author=u4, timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # c1 = Comment(body='Comment #1', timestamp=now, author_id=1, post_id=1)
        # c2 = Comment(body='Comment #2', timestamp=now, author_id=2, post_id=2)
        # c3 = Comment(body='Comment #3', timestamp=now, author_id=3, post_id=3)
        # c4 = Comment(body='Comment #4', timestamp=now, author_id=4, post_id=4)
        # db.session.add_all([c1, c2, c3, c4])
        

if __name__ == '__main__':
    unittest.main(verbosity=2)
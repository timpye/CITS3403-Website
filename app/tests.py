import unittest
from app import app, db
from app.models import User, Result

class UserModelCase(unittest, TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username="john")
        u.set_password('doggy')
        self.assertTrue(u.check_password('doggy'))
        self.assertFalse(u.check_password('style'))
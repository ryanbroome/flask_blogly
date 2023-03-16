from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_test_db'
app.config['SQLALCHEMY_ECHO'] = False

#? connect_db(app)

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self):
        """Clean up any existing Users."""

        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_user_first_name(self):
        user = User(first_name='Test', last_name="User", image_url="test_image")
        self.assertEqual(user.first_name, 'Test')

    def test_full_name(self):
        user = User(first_name='Test', last_name="User", image_url="test_image")
        full_name = user.full_name(user.id)
        self.assertIn(full_name, "Test User")

    def test_get_user_by_id(self):
       user = User(first_name='Test', last_name="User", image_url="test_image")
       test_user = user.get_by_id(user.id)
       self.assertEqual(test_user.first_name, "Test")

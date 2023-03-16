"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.init_app(app)
    db.app = app
    app.app_context().push()

class User(db.Model):
    """User"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String(100), nullable=False)

    last_name = db.Column(db.String(30), nullable=False)

    image_url = db.Column(db.String, nullable=True, default='/static/sample.jpeg')

    @classmethod
    def full_name(cls, id):
        user = cls.query.get(id)
        return f"{user.first_name} {user.last_name}"

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    def __repr__(self):
        u = self
        return f"<User id={u.id} first={u.first_name} last={u.last_name} imageURL={u.image_url}>"

    def greet(self):
        """return greeting of each Pet"""
        return f"Hi, I am {self.first_name} {self.last_name} and my user id is {self.id}, I have a pic here {self.image_url}"

    def add_image(self, image_url):
        """Update hunger based off of amt"""
        self.image_url = image_url

        # if trying to make updates to a table like adding a column, go to postgres and DROP TABLE, it will not create a table if the same table already exists in the db

"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from datetime import date
# from datetime import time

db = SQLAlchemy()

# getting current pretty time
def stamp():
    """generate a pretty date stamp"""
    dt = datetime.now()
    return dt.strftime("%a %b %-d %Y, %-I:%M %p")

def connect_db(app):
    db.init_app(app)
    db.app = app
    app.app_context().push()

class User(db.Model):
    """User table"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String, nullable=True, default='/static/sample.jpeg')

    posts = db.relationship("Post", backref='user', cascade='all, delete')

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

        #* if trying to make updates to a table like adding a column, go to postgres and DROP TABLE, it will not create a table if the same table already exists in the db

class Post(db.Model):
    """Post"""
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(2500), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=stamp())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    def __repr__(self):
        p = self
        return f"<post id={p.id} post title={p.title} created_at={p.created_at} user_id={p.user_id} content=''>"

class PostTag(db.Model):
    """PostTag two column primary key both foreign key"""

    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), primary_key=True)

    tag_id = db.Column(db.Integer, db.ForeignKey(
        'tags.id'), primary_key=True)
    
    db.UniqueConstraint('post_id', 'tag_id', name='uq_post_tag')

class Tag(db.Model):
    """Tag"""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    posts = db.relationship('Post', secondary='posts_tags', cascade='all, delete', backref='tags')

    def __repr__(self):
        t = self
        return f"< tag id:  {t.id},  tag name:  {t.name} >"
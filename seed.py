'''Seed file to make sample data for pets db.'''

# todo update from models import Class_name, db 
from models import User
from models import Post
from models import db
from app import app

#? CREATE DATABASE / TABLES init 

db.drop_all()
db.create_all()

# ? If table isnt empty, empty it TODO update Class_name.query.delete() 
User.query.delete()
Post.query.delete()

# ? ADD INSTANCES OF db.Models such as Pets
ryan = User(first_name ='Ryan', last_name ='Broome', image_url='/static/sample.jpeg')
betsy = User(first_name ='Betsy', last_name ='Broome', image_url='/static/betsy.jpeg')
avery = User(first_name ='Avery', last_name ='Broome', image_url='/static/avery.jpeg')
roman = User(first_name ='Roman', last_name ='Broome', image_url='/static/sample.jpeg')
leia = User(first_name ='Leia', last_name ='Broome', image_url='/static/leah.jpeg')

first = Post(title='Test Post One', content='This is my first post', user_id=1)
second = Post(title='Test Post Two', content='SECOND IS THE BEST, THIRD IS THE ONE WITH THE HAIRY CHEST', user_id=1)
third = Post(title='Test Post Three', content='This is a post about stuff', user_id=2)

# todo update object adds with instances from above, used db.session.add_all()
# ? Add new instances of objects to db.session, so they'll persist until next commit, unless you use db.session.rollback()
db.session.add_all([ryan, betsy, avery, roman, leia])
db.session.add_all([first, second, third])


# ? Commit -- otherwise, this never gets saved to db!
db.session.commit()

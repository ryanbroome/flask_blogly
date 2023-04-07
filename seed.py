'''Seed file to make sample data for pets db.'''

# todo update from models import Class_name, db 
from models import User
from models import Post
from models import Tag
from models import PostTag
from models import db
from app import app

#? CREATE DATABASE / TABLES init 

db.drop_all()
db.create_all()

# ? If table isnt empty, empty it TODO update Class_name.query.delete() 
User.query.delete()
Post.query.delete()
Tag.query.delete()
PostTag.query.delete()


# ? ADD INSTANCES OF db.Models such as Users, Posts, Tags, PostTags 
ryan = User(first_name ='Ryan', last_name ='Broome', image_url='/static/sample.jpeg')
betsy = User(first_name ='Betsy', last_name ='Broome', image_url='/static/betsy.jpeg')
avery = User(first_name ='Avery', last_name ='Broome', image_url='/static/avery.jpeg')
roman = User(first_name ='Roman', last_name ='Broome', image_url='/static/sample.jpeg')
leia = User(first_name ='Leia', last_name ='Broome', image_url='/static/leah.jpeg')

first_post = Post(title='Test Post One', content='Ryans first post', user_id=1)
second_post = Post(title='Test Post Two', content='Ryans second post', user_id=1)
third_post = Post(title='Test Post Three', content='Betsy first post', user_id=2)

like = Tag(name='like')
safe = Tag(name='safe')
work = Tag(name='work')
daily = Tag(name='daily')
home = Tag(name='home')


# todo update object adds with instances from above, used db.session.add_all()
# ? Add new instances of objects to db.session, so they'll persist until next commit, unless you use db.session.rollback()
db.session.add_all([ryan, betsy, avery, roman, leia])
db.session.add_all([first_post, second_post, third_post])
db.session.add_all([like, safe, work, daily, home])



# ? Commit -- otherwise, this never gets saved to db!
db.session.commit()

pt = PostTag(post_id=1, tag_id=1 )
pt2 = PostTag(post_id=1, tag_id=2 )
pt3 = PostTag(post_id=1, tag_id=3 )

db.session.add_all([pt, pt2, pt3])
db.session.commit()
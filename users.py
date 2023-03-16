'''Seed file to make sample data for pets db.'''

# todo update from models import Class_name, db 
from models import User
from models import db
from app import app

#? CREATE DATABASE

# ? CREATE ALL TABLES
db.drop_all()
db.create_all()

# todo update Class_name.query.delete() below
# ? If table isnt empty, empty it
User.query.delete()

# todo update instances to match models
# ? ADD INSTANCES OF db.Models such as Pets
ryan = User(first_name ='Ryan', last_name ='Broome', image_url='static/pic.jpg')
betsy = User(first_name ='Betsy', last_name ='Broome', image_url='static/pic.jpg')
avery = User(first_name ='Avery', last_name ='Broome', image_url='static/pic.jpg')
roman = User(first_name ='Roman', last_name ='Broome', image_url='static/pic.jpg')


# todo update object adds with names of instances from above
# ? Add new instances of objects to db.session, so they'll persist until next commit, unless you use db.session.rollback()
db.session.add(ryan)
db.session.add(betsy)
db.session.add(avery)
db.session.add(roman)

# ? Commit -- otherwise, this never gets saved to db!
db.session.commit()

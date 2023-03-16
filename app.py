"""Blogly application."""
from models import db
from models import connect_db
from models import User

from flask import Flask
from flask import current_app
from flask import redirect 
from flask import render_template 
from flask import request
from flask import session

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///users_db"

app.config['SECRET_KEY'] = 'superSecretPassword'

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.config["SQLALCHEMY_ECHO"] = True

app.config["SQLALchemy_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

# HOME PAGE
@app.route('/')
def show_base():
    """Show base page / home page"""
    return render_template('base.html')

# GET list of all users
@app.route('/users')
def list_users():
    """show home page"""
    users = User.query.all()
    return render_template('list.html', users=users)

# GET /users/new
@app.route('/users/new')
def show_add_form():
    """show add user form page"""
    return render_template('add_form.html')

# POST /users/new 
@app.route('/users/new', methods=["POST"])
def create_user():
    """Add new user to the database"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")

# GET /users/[user-id]]
@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

# GET /users/{user.id}/edit
@app.route('/users/<int:user_id>/edit')
def show_edit_form(user_id):
    """Edit details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_form.html", user=user)

# POST /users/{user.id}/edit
@app.route('/users/<int:user_id>/edit', methods=["POST"])
def edit_user(user_id):
    """Edit details about a single user"""
    user = User.query.get_or_404(user_id)

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    if len(first_name) > 0:
        user.first_name = first_name

    if len(last_name) > 0:
        user.last_name = last_name
    
    if len(image_url) > 0:
        user.image_url = image_url

    db.session.add(user)
    db.session.commit()
    return redirect('/users')

#POST /users/{user.id}/delete
@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete user from db"""

    user =User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')

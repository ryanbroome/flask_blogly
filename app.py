"""Blogly application."""
from models import db
from models import connect_db
from models import User
from models import Post

from flask import Flask
from flask import current_app
from flask import redirect 
from flask import render_template 
from flask import request
from flask import session

from flask_debugtoolbar import DebugToolbarExtension

from datetime import datetime, date, time

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///users_db"

app.config['SECRET_KEY'] = 'superSecretPassword'

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.config["SQLALCHEMY_ECHO"] = True

app.config["SQLALchemy_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

# getting current date time in a nicer format
def stamp():
    """generate a pretty date stamp"""
    dt = datetime.now()
    return dt.strftime("%A, %B %d %Y at %I:%M%p")

# HOME PAGE
@app.route('/')
def show_base():
    """Show base page / home page"""
    p = Post.query
    posts = p.all()
    post_count = len(posts)

    recent_posts = p.filter(Post.id >= (post_count -5))
    
    return render_template('base.html', recent_posts=recent_posts)

# GET list of all users
@app.route('/users')
def list_users():
    """show home page"""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('list.html', users=users)

# GET /users/new
@app.route('/users/new')
def show_add_user_form():
    """show add user form page"""
    return render_template('add_user_form.html')

# GET /users/[user_id]/posts/new
@app.route('/users/<int:user_id>/posts/new')
def show_add_post_form(user_id):
    """show add post form page"""
    user = User.query.get_or_404(user_id)
    return render_template('add_post_form.html', user=user)

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

# POST /users/{user_id}/posts/new
@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def create_post(user_id):
    """Add new post to the database"""
    add_title = request.form["add_title"]
    add_content = request.form["add_content"]

    new_post = Post(title=add_title, content=add_content, user_id=user_id )

    db.session.add(new_post)
    db.session.commit()
    # user = User.query.get_or_404(user_id)
    return redirect(f"/users/{user_id}")

# GET /users/[user-id]]
@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about a single user"""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user_id)
    time = stamp()
    return render_template("details.html", user=user, posts=posts, time=time)

# GET /posts/[post-id]]
@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show details about a single post"""
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)

    return render_template("post_details.html", post=post, user=user)

# GET /users/{user.id}/edit
@app.route('/users/<int:user_id>/edit')
def show_edit_user_form(user_id):
    """Edit details about a single user"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_user_form.html", user=user)

# GET /posts/{post.id}/edit
@app.route('/posts/<int:post_id>/edit')
def show_edit_post_form(post_id):
    """Edit details about a single post"""
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    return render_template("edit_post_form.html", post=post, user=user)

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

# POST /posts/{post.id}/edit
@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def edit_post(post_id):
    """Edit details about a single post"""
    post = Post.query.get_or_404(post_id)

    title = request.form["title"]
    content = request.form["content"]

    if len(title) > 0:
        post.title = title

    if len(content) > 0:
        post.content = content
    
    db.session.add(post)
    db.session.commit()
    return redirect(f'/posts/{post.id}')

#POST /users/{user.id}/delete
@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Delete user from db"""

    user =User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')

#POST /users/{user.id}/delete
@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Delete post from db"""
    post =Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')

# todo Styling, work on css positioning, add a navbar / footbar, home page with 5 most recent posts
# todo TESTING not working, not detecting tests, maybe old version of python?
# todo REFACTOR, REDUCE ANY DUPLICATION. SEE IF ANY FORMS OR OTHER CODE BLOCKS CAN BE REUSED?? Seems like edit forms could be automated since similar. 
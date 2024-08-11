from flask import Flask, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

# Routing
@app.route("/")
def index():
    return "Index Page"
# Testing <variables>
@app.route("/hello-world")
def hello():
    return "Hello, World!"
@app.route("/user/<username>")
def show_user_profile(username):
    return f'User ({escape(username)})'

@app.route("/post/<post_id>")
def show_post_id(post_id):
    return f'Post ({escape(post_id)})'

# Unique URLs/Redirection
@app.route("/projects/")
def projects():
    return "Projects Page"

@app.route("/about")
def about():
    return "About Page"

# HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
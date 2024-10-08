from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape

app = Flask(__name__)

# Routing
@app.route("/")
def index():
    return "Index Page"
# Testing <variables>
# @app.route("/hello-world")
# def hello():
#     return "Hello, World!"
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

# Adding Templates
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', person=name)

# Render Templates
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    navigation = [
        {'href': '#home', 'caption': 'Home'},
        {'href': '#about', 'caption': 'About'},
        {'href': '#contact', 'caption': 'Contact'},
        {'href': url_for('portfolio'), 'caption': 'Portfolio'},
        {'href': url_for('ninja'), 'caption': 'Ninja'},
    ]
    a_variable = f"Hello, {name}!" if name else "Welcome to My Webpage!"

    return render_template('hello.html', navigation=navigation, a_variable=a_variable)


@app.route('/portfolio')
def portfolio():
    cards = [
        {
            'title': 'Docker',
            'description': 'Docker is a platform for developing, shipping, and running applications in containers.',
            'image': 'https://cdn.iconscout.com/icon/free/png-256/free-docker-12-1175229.png'
        },
        {
            'title': 'Kubernetes',
            'description': 'Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/3/39/Kubernetes_logo_without_workmark.svg'
        },
        {
            'title': 'Jenkins',
            'description': 'Jenkins is an open-source automation server used to build, test, and deploy software.',
            'image': 'https://www.jenkins.io/images/logos/jenkins/jenkins.svg'
        },
        {
            'title': 'Ansible',
            'description': 'Ansible is an open-source tool for IT automation, configuration management, and app deployment.',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/2/24/Ansible_logo.svg'
        }
    ]
    return render_template('portfolio.html', cards=cards)

@app.route('/ninja/')
def ninja():
    jiraiya_facts = [
        {
            'title': 'Legendary Sannin',
            'description': 'Jiraiya is one of the Legendary Sannin, a group of three powerful ninjas trained by the Third Hokage, Hiruzen Sarutobi.'
        },
        {
            'title': 'Author of Icha Icha',
            'description': 'Jiraiya is the author of the popular adult book series "Icha Icha," which is often read by Kakashi Hatake.'
        },
        {
            'title': 'Mentor to Naruto Uzumaki',
            'description': 'Jiraiya served as a mentor to Naruto Uzumaki, helping him learn powerful techniques like the Rasengan and summoning jutsu.'
        },
        {
            'title': 'Toad Sage',
            'description': 'Jiraiya was known as the Toad Sage because of his ability to summon toads and his mastery of Sage Mode, taught to him by the Great Toad Sage in Mount Myoboku.'
        }
    ]

    # Render the ninja.html template and pass the facts to it
    return render_template('ninja.html', facts=jiraiya_facts)  # Render the first fact as an example

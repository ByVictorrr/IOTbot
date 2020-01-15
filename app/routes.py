from flask import render_template, url_for
from app import app_instance

from forms import RegistrationForm, LoginForm



posts = [
    {
        'author': 'Victor Delaplaine',
        'title': 'blog post 1',
        'content': "first post content",
        'date_posted': "April 20, 2010",

    },
    {
        'author': 'Victor Delaplaine',
        'title': 'blog post 2',
        'content': "2nd post content",
        'date_posted': "April 21, 2010",

    }
]

@app_instance.route('/')
@app_instance.route('/home')
@app_instance.route('/login')
def home():
    return render_template("home.html",posts=posts)


@app_instance.route('/about')
@app_instance.route('/FAQ')
@app_instance.route('/usage')
def others():
    return render_template("about.html")


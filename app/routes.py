from flask import render_template, url_for
from app import app_instance
from app.forms import LoginForm, RegistrationForm




@app_instance.route('/')
@app_instance.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title='Login',form=form)

@app_instance.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)




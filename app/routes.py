from flask import render_template, url_for, request, flash
from app import app_instance, login
from flask_login import current_user, login_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse
from app import db


import pdb


@app_instance.route('/')
def home():
    return render_template('home.html', title=home)

@app_instance.route('/login',methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("login.html", title='Login',form=form)

@app_instance.route('/logout')
def logout():
    login_user()
    return redirect(url_for('home'))

@app_instance.route('/register', methods=['POST', 'GET'])
def register():
    breakpoint()
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        breakpoint()
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user")
        return redirect(url('login'))
    return render_template('register.html',title='Register', form=form)






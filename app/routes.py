from flask import render_template, url_for
from app import app_instance, login
from flask_login import current_user, login_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User




@app_instance.route('/')
def home():
    return render_template('home.html', title=home)

@app_instance.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template("login.html", title='Login',form=form)

@app_instance.route('/logout')
def logout():
    login_user()
    return redirect(url_for('home'))

@app_instance.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)




@app_instance("/IOTbot")
@login_required
def controller():
    return None


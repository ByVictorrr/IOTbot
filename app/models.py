from datetime import datetime
from app import db, login
from flask_login import UserMixin 

# login function the manager expects the model to have

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# linking the login to load a user
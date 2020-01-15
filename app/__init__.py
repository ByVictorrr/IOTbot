""" This folder tells python that this folder should be treated as a package """
from flask import Flask

# __name__ for __init__.py file is the parent folder
app_instance=Flask(__name__)

# From our app package import routes
from app import routes


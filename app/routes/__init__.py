from flask import Flask
from .user_blueprint import bp as bp_user

def init_app(app:Flask):
    app.register_blueprint(bp_user)

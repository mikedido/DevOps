from flask import Flask
from .routes import home

def register_blueprints(app):
    app.register_blueprint(home)

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
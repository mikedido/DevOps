from flask import Flask, Blueprint

home = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

@home.route('/')
def hello():
    return 'hello world'

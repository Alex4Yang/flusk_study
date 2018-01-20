from flask import render_template

from . import routes


@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/hello/<user>')
def hello(user):
    return render_template('hello.html', name=user)



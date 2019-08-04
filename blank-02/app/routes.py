from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Faby'}
    posts = [
        {'author': {'username': 'Thiago'}, 'body': 'Beautiful day in Portland!'},
        {'author': {'username': 'Fabiana'}, 'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

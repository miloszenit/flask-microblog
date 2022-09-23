from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Milos'}
    posts = [
        {
            'author': {'username': 'Michael'},
            'body': 'I will get up early in the morning!'
        },
        {
            'author': {'username': 'Isabella'},
            'body': 'Have a nice day!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

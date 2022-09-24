from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Test message: user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Login', form=form)

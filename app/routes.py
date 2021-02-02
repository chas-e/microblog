from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chas'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'A Beautiful Day in Portland!'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'That new Amazon show "Flack" is da bomb!'
        },
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


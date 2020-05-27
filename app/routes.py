from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bibi'}
    posts = [
        {
            'author': {'username': 'Cat'},
            'body': 'Need help with flask!'
        },
        {
            'author': {'username': 'Bob'},
            'body': 'How do I use Azure API?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

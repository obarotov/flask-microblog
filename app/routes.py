from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Otabek'}
    posts = [
        {
            'author': {'username': 'Abdulaziz'},
            'body': 'Beautiful day in Tajikistan!'
        },
        {
            'author': {'username': 'Ahmadjon'},
            'body': 'The Invincible series was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
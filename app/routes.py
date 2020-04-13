from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Ares"}
    posts = [
        {
            'author': {'username': 'Cathy'},
            'body': 'Beautiful day indoors!'
        },
        {
            'author': {'username': 'Trevor'},
            'body': 'BoJack Horseman is so cool!'
        }
    ]
    return render_template("index.html", title="Ares is a good cat", user=user, posts=posts)
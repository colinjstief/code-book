"""Simple Flask server"""

from flask import Flask, render_template, url_for

APP = Flask(__name__)

@APP.route('/')
def homepage():
    """Render homepage"""
    info = {
        "title": "Homepage",
        "message": "Hello there!",
        "itemList": [
            "First item",
            "And another item",
            "Still one more"
        ]
    }

    return render_template('home.html', pageInfo=info)

@APP.route('/about')
def about():
    """Render about page"""
    return render_template('about.html')

## Change port here
APP.run(port=4995)

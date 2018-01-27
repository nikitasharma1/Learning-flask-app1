#!/usr/bin/python3

# Import from flask
from flask import Flask, render_template

# Create Flask instance
app = Flask(__name__)


# Home page
@app.route('/')
def index():
    return render_template('index.html')


# About page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    port = 5000

    # Use stronger secret in production env
    app.secret_key = 'somesecretkey'
    # Run app at default port 5000
    app.run(host='0.0.0.0', port=port)

    # Turn off debugging in production env
    app.debug = True

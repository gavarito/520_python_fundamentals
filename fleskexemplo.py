#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return '<h1>Ola mundo </h1>'

@app.route('/login')
def login():
    return '<h1> Area de login </h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

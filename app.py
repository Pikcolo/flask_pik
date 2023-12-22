from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/me')
def my_name():
    return 'Sirawich Noipha'
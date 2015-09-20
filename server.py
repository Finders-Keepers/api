from flask import Flask
from flask import request
from flask import jsonify
import requests
import json

app = Flask(__name__)

gps_data = ""
accelerometer_data = []

@app.route('/')
def index():
    return 'Welcome Home'

@app.route('/push', methods=['GET', 'POST'])
def push():
    if request.method == 'POST':
        print request.form
    else:
        pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    ret = {}
    if username == 'kadajett' and password == 'password':
        ret['thing'] = 'other thing'
        return jsonify(**ret)
    else:
        abort(401)

@app.route('/track')
def track():
    pass



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

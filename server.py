from flask import Flask
import requests

app = Flask(__name__)

gps_data = ""
accelerometer_data = []

@app.route('/')
def index():
    return 'Welcome Home'

@app.route('/push', methods=['GET', 'POST'])
def push():
    if request.method == 'POST':
        pass
    else:
        pass

@app.route('/track')
def track():
    pass



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

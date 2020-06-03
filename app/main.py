from flask import Flask
from RPi import GPIO 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

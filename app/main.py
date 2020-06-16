from flask import Flask, jsonify
from flask_cors import CORS
import gpiozero as gp
app = Flask(__name__)

CORS(app)

@app.route('/get_state')
def get_state():
    return jsonify({'status':'on'})

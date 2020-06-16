from flask import Flask, jsonify
import gpiozero as gp
app = Flask(__name__)


@app.route('/get_state')
def get_state():
    return jsonify({'status':'on'})

from flask import Flask, render_template, request, current_app as current_app
from sense_emu import SenseHat
import sqlite3

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Project is Running<p>"

@app.route('/pomodoro')
def main():
    return render_template('/pomodoro.html')
    
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
from flask import Flask, render_template, request, current_app as current_app
from sense_hat import SenseHat
import sqlite3

sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/pomodoro')
def main():
    return render_template('/pomodoro.html')

@app.route('/theme')
def theme():
    return render_template('/theme.html')

@app.route('/entryType')
def entry():
    return render_template('/entryType.html')

@app.route('/fitness')
def fitness():
    return render_template('/fitness.html')

@app.route('/dream')
def dream():
    return render_template('/dream.html')





@app.route('/journal')
def journal():
    return render_template('/journal.html')
    
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
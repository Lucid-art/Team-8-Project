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

@app.route('/everyday')
def everyday():
    conn = sqlite3.connect('./static/store/journal.db')
    curs = conn.cursor()
    journal = []
    message = {'entries': row[1], 'rowid': row[0]}
    return render_template('/everyday.html')

@app.route('/guided')
def guided():
    return render_template('/guided.html')
    
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
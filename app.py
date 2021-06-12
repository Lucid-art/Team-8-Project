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

@app.route('/store', methods=["POST"])
def store():
    title = request.form['entry-title']
    daily = request.form['daily-entry']
    conn = sqlite3.connect('./static/data/journal.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO entries(name, entries) VALUES((?), (?))",(title,daily))
    conn.commit()
    conn.close()
    return render_template('/everyday.html')






@app.route('/everyday')
def day():
    #connecting to database
    conn = sqlite3.connect('./static/data/journal.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM  entries")
    conn.commit()
    #close database connection
    conn.close()
    return render_template('/everyday.html')
    
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
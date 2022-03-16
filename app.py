import sqlite3

from flask import Flask, render_template, request, flash, url_for

db = 'docs.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = '1fishtwofishblowfishbluefish23'

def get_db_connection(db):
    """ """
    conn = sqlite3.connect(str(db))
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    db_notes = conn.execute('SELECT * FROM docs').fetchall()
    conn.close()

    notes = []

    for note in db_notes:
        note = dict(note)
        notes.append(note)

return render_template("index.html")


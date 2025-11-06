# Rohan Sen, Haowen Xiao, Michelle Chen, Aoanul Hoque
# HeistLEET
# SoftDev
# P00
# 2025-10-28
# time spent: 0.67

from flask import Flask  # facilitate flask webserving
from flask import render_template  # facilitate jinja templating
from flask import request, redirect, url_for  # facilitate form submission
from flask import session
import sqlite3
from cryptography.fernet import Fernet as crypt

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()

c.execute("create table if not exists students(name text, age integer, id integer primary key);")
c.execute("create table if not exists courses(code text, mark integer, id integer);")

app = Flask(__name__)  # create Flask object
app.secret_key = b'sixseven'
key = crypt.generate_key()
crypto = crypt(key)
def fetch_creds(usr, pass_unc):
    accounts = c.execute(f"select name from students where username = {usr} and password = {crypto.encrypt(pass_unc)};")
    if len(accounts = 0):
        return -1
    return accounts[0]

@app.route("/", methods=['GET', 'POST'])
def response():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        session.permanent = True
        session['username'] = request.form['id']
        
        return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route("/home", methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
        return render_template('logout.html')
    return redirect(url_for('login'))


if __name__ == "__main__":  # false if this file imported as module
    app.debug = True  # enable PSOD, auto-server-restart on code chg
    app.run()

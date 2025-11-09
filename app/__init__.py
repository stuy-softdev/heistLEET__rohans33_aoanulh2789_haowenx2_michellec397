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
from datetime import datetime
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False) #open if file exists, otherwise create
db.row_factory = sqlite3.Row
c = db.cursor()

c.execute("create table if not exists entries(user_id integer, title text, post text, timestamp date, last_edit date, id integer primary key);")
c.execute("create table if not exists account(username text, email text, password text, first_name text, last_name text, img_path text, id integer primary key);")
db.commit()

app = Flask(__name__)  # create Flask object
app.secret_key = b'sixseven'
def fetch_creds(usr, pass_unc):
    account = c.execute("select * from account where username = ?", (usr,)).fetchone()
    if not account:
        return False
    return check_password_hash(account['password'], pass_unc)

def set_creds(usr, pass_unc):
    if c.execute("select * from account where username = ?", (usr,)).fetchone() is None:
        c.execute("insert into account (username, password) values (?, ?);", (usr, generate_password_hash(pass_unc,method='pbkdf2')))
        db.commit()
        return True
    else:
        return False

def post(username, title, content):
    #fetch user id from the account table
    user = c.execute("select id from account where username = ?"), (username,).fetchone()
    if user:
        user_id = user['id']
        current_dateTime = datetime.datetime.now()
        print(current_dateTime)#should print year, month, day, hour, minute, second, etc.
        c.execute("""insert into entries (user_id, title, post, timestamp, last_edit)
         values (?, ?, ?, ?, ?);""",(username, title, content, timestamp, timestamp))
         db.commit()

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
        if fetch_creds(request.form['id'], request.form['pass']):
            session.permanent = True
            session['username'] = request.form['id']
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        set_creds(request.form['username'], request.form['pass'])
        return redirect(url_for('login'))
    else:
        return render_template('signup.html')

@app.route("/home", methods=['GET', 'POST'])
def home():
    if 'username' in session:
        #should post everything to home page in order of dates
        posts = c.execute("SELECT * FROM entries ORDER BY timestamp DESC;").fetchall()
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route("/new", methods=['GET', 'POST'])
def create():
    if 'username' in session:
        if request.method == 'POST':
            post(session["username"], request.form['title'], request.form['content'])
            return redirect(url_for('home'))
        return render_template('create.html', username=session['username'])
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

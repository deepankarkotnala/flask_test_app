from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import argparse

# Setting up an admin password
# Default password is "password"

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pwd", required=False, default='password', help="Set admin password")
args = vars(ap.parse_args())
admin_pwd = args['pwd']

app = Flask(__name__)
@app.route("/")

def home():
    if not session.get('logged_in'):
        return render_template('login_page.html')
    else:
        return render_template("home.html")

@app.route("/login", methods=['POST'])
def do_admin_login():
    if session.get('logged_in'):
        return render_template("home.html")
    if request.form['password'] == admin_pwd and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template("home.html")
    else:
        flash('wrong password!')
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/signup")
def signup():
    return render_template("signup_page.html")

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
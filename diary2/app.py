import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///digidiary.db")

# Home
@app.route("/")
def index():

    return render_template("index.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")


    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        password = request.form.get("password")
        username = request.form.get("username")
        confirmation = request.form.get("confirmation")

        # Check if there is a username input
        if not username:
            return apology("No username")

        # Check if there is a password input
        elif not password:
            return apology("No password")

        # Password must be at least 6 characters long
        if len(password) < 6:
            return apology("Password must be at least 6 characters long")

        # Password must have at least 1 number
        if not any(char.isdigit() for char in password):
            return apology("Password must have at least 1 number")

        # Password has to have at least 1 special symbol
        special = ['!', '@', '$', '#', '%', '^', '&']
        if not any(char in special for char in password):
            return apology("Password must contain at least 1 special symbol from the following: !@#$%^&")

        # Check if the password and confirmation passwords match
        elif password != confirmation:
            return apology("Passwords must match")

        # Put user into users table, username must be one not taken already
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(rows) != 0:
            return apology("Username is taken")

        id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        session["user_id"] = id
        flash("Successfully registered!")
        return redirect("/")

    else:
        return render_template("register.html")

# Create diary entries
@app.route("/create", methods=["GET", "POST"])
def create():

    # Need to collect data input to create diary form
    if request.method == "POST":
        title = request.form.get("title")
        date = request.form.get("date")
        content = request.form.get("content")
        mood = request.form.get("mood")

        # Every part of the form must be filled out
        if not request.form.get("title"):
            return apology("Title required")
        if not request.form.get("date"):
            return apology("Date required")
        if not request.form.get("content"):
            return apology("Main entry required")
        if not request.form.get("mood"):
            return apology("Mood entry required")

        # Update our diary table
        db.execute("INSERT INTO diary (user_id, date, title, content, mood) VALUES(?, ?, ?, ?, ?)", session["user_id"], date, title, content, mood)

        flash("New entry created!")
        return redirect("/entries")

    else:
        return render_template("create.html")

@app.route("/entries")
@login_required
def entries():
    rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    if not rows:
        return apology("Error")

    diaries = db.execute("SELECT * FROM diary where user_id = ?", session["user_id"])
    return render_template("entries.html", diaries=diaries)

# Settings page
@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    return render_template("settings.html")

# Change password
@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    if request.method == "GET":
        return render_template("changepassword.html")
    else:
        # Set our variables
        user_id = session["user_id"]
        new = request.form.get("new")
        old = request.form.get("old")
        confirmation = request.form.get("confirmation")

        # Obtain hash of password
        rows = db.execute("SELECT hash FROM users WHERE id = ?", user_id)

        # New password must be at least 6 characters long
        if len(new) < 6:
            return apology("Password must be at least 6 characters long")

        # New password must have at least 1 number
        if not any(char.isdigit() for char in new):
            return apology("Password must have at least 1 number")

        # New password has to have at least 1 special symbol
        special = ['!', '@', '$', '#', '%', '^', '&']
        if not any(char in special for char in new):
            return apology("Password must contain at least 1 special symbol from the following: !@#$%^&")

        # Passwords must match
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], old):
            return apology("Old password incorrect.")
        if new != confirmation:
            return apology("Passwords do not match.")

        # Update new password
        hash = generate_password_hash(new)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, user_id)

        flash("Successfully changed!")
        return redirect("/")
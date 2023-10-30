from datetime import timedelta, datetime

from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

from second.second import second

app = Flask(__name__)

# Register bluepring app
app.register_blueprint(second, url_prefix="/second/")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "dsjio3*&$*(^#xec]/"
app.permanent_session_lifetime = timedelta(minutes=50)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", name=user)
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        flash("You were successfully logged in", "success")
        return redirect(url_for("user", name=user))
    else:
        if "user" in session:
            flash("You are already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/logout")
def logout():
    """remove the name from the session if it's there"""

    session.pop("user", None)
    flash("You were successfully logged out")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

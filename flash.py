import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"

@app.route("/", methods=["POST","GET"])

def home():
    if request.method=="POST":
        email=request.form["email"]
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        return render_template("output.html", first_name =first_name, last_name=last_name, email=email)
    else:
        return render_template("index.html")

@app.route("/page")
def page():
    return "<h1> test </h1>"
if __name__ == '__main__':
    app.run()


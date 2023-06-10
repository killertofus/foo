import sqlite3
import smtplib
import random
import os
from dotenv import load_dotenv
from flask import Flask, session, render_template, request, g

load_dotenv()

conn = sqlite3.connect('customer.db')
cur = conn.cursor()

app = Flask(__name__)
app.secret_key = "select_a_COMPLEX_secret_key_please"

@app.route("/", methods=["POST","GET"])


def home():
    conn = sqlite3.connect('customer.db')
    cur = conn.cursor()    

    if request.method=="POST":
        email=request.form["email"]
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        cur.execute("insert into customer (last_name, first_name , email) values(?, ?, ?)", [last_name, first_name , email]);
        message = ("test")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("cinemassacres@gmail.com", os.getenv("password"))
        server.sendmail("cinemassacres@gmail.com", email, message)
        conn.commit()
        return render_template("output.html", first_name =first_name, last_name=last_name, email=email)
    else:
        return render_template("index.html")

@app.route("/page")
def page():
    return "<h1> test </h1>"
if __name__ == '__main__':
    app.run()


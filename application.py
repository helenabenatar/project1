from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if not request.form.get("name") or not request.form.get("lastname") or not request.form.get("university"):
        return render_template("failure.html")
    file = open("survey.csv", "a")
    writer = csv.writer(file)
    writer.writerow(((request.form.get("name"), request.form.get("lastname"), ("university"))))
    file.close()
    return render_template("success.html")

@app.route("/harvard.html")
def harvard():
    return render_template("harvard.html")

@app.route("/brown.html")
def brown():
    return render_template("brown.html")

@app.route("/yale.html")
def yale():
    return render_template("yale.html")
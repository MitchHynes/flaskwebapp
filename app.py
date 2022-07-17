from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html") 

@app.route("/blog")
def linux_blog(post=None):
    return render_template("linuxblog.html")

@app.route("/about")
def about():
    return render_template("about.html")


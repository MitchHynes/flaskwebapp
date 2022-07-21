from flask import Flask, url_for, redirect, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "slthwoyofmaWTSWPDLEYTYHSHWTHSHJFAWOdaoufowue"
#add a datebase, sqlite right now, could swap it out with something else like mysql
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"

db = SQLAlchemy(app)

#create a model, every database needs a moder
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(255))

    def __repr__(self):
        return "<Title %r>" % self.title

@app.route("/posts")
def posts():
    #Grab all the posts from the database
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template("post.html", posts=posts)


@app.route("/")
def hello_world():
    return render_template("index.html") 

@app.route("/blog")
def linux_blog(post=None):
    return render_template("linuxblog.html")

@app.route("/about")
def about():
    return render_template("about.html")


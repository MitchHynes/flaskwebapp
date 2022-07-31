from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
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
@app.route("/posts/<int:id>")
def post(id):
    post = Posts.query.get_or_404(id)
    return render_template("post.html", post=post)


@app.route("/posts")
def posts():
    #Grab all the posts from the database
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template("posts.html", posts=posts)


@app.route("/")
def blog():
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template("index.html", posts=posts) 

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#temporary methods to manage the database, replace with a better way 
#call them from the python interpreter
#when I learn a better way in databases course
def add_post(post_title, post_content):
    post = Posts(title=post_title, content=post_content)
    db.session.add(post)
    db.session.commit()

def delete_post():
    posts = Posts.query.order_by(Posts.date_posted)
    for post in posts:
        db.session.delete(post)
    db.session.commit()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')

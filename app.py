from flask import Flask, url_for, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "slthwoyofmaWTSWPDLEYTYHSHWTHSHJFAWOdaoufowue"

#create a form class
class NamerForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/")
def hello_world():
    return render_template("index.html") 

@app.route("/blog")
def linux_blog(post=None):
    return render_template("linuxblog.html")

@app.route("/about")
def about():
    return render_template("about.html")

#create name page
@app.route("/name", methods=["GET","POST"])
def name():
    name = None
    form = NamerForm()
    #validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = "" #clear it for the next time around

    return render_template("name.html", name=name, form=form)

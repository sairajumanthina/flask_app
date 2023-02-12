from flask import Flask,render_template
from users import return_users_data
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/users")
def users():
    return render_template("users.html",users=return_users_data())
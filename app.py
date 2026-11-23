from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> <img src='' />"
    

@app.route("/")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, Kia!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #21"


from flask import Flask, request, render_template
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

#Route untuk menampilkan form
@app.route("/form")
def form():
    return render_template("index.html")

#Route untuk menerima data POST
@app.route("/proses", methods=["POST"])
def proses():
    nama = request.form.get("nama")
    return render_template("index.html", hasil=nama)
  if __name__ == "__main__":
    app.run(debug=True)

#Buat index HTML

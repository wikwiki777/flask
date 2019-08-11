import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
# View name index
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=5000, debug=True)

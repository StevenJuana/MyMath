from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lessons/")
def lessons():
    return render_template("lessons.html")

if __name__ == "__main__":
    app.run(debug=True)
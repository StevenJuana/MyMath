from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "this is the initial home page <h1> TEST </h1>"

if __name__ == "__main__":
    app.run(debug=True)
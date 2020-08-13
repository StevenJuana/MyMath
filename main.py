from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "this is the initial home page"

if __name__ == "__main__":
    app.run(debug=True)
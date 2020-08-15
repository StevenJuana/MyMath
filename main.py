# main.py

# This is the main file for the project. This file contains the logic to route
# to certain pages, as well as logic to generate and solve each problem.

from flask import Flask, render_template

from addSubMult import addSubMult
from division import division
from algebra import algebra
from geometry import geometry


# Creates a flask app
app = Flask(__name__)

# Register the blueprints for the related modules
app.register_blueprint(addSubMult, url_prefix="")
app.register_blueprint(division, url_prefix="")
app.register_blueprint(algebra, url_prefix="")
app.register_blueprint(geometry, url_prefix="")

# Creates a secret key for the program
app.secret_key = "GarudaHacks4Ever"


@app.route("/")
def home():
    """Takes user to the home page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

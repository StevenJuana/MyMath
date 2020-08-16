# main.py

# This is the main file for the project. This file contains the logic to route
# to the home page, as well as establishes all of the Blueprints for the other
# pages in the project

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


@app.route("/")
def home():
    """Takes user to the home page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

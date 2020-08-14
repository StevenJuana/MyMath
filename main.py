from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/lessons/")
def lessons():
    return render_template("lessons.html")


@app.route("/additionEasy")
def addition_easy():
    return render_template("equation1.html", problem_type="addition", difficulty="easy")


@app.route("/additionIntermediate")
def addition_intermediate():
    return render_template("equation1.html", problem_type="addition", difficulty="intermediate")


@app.route("/additionAdvanced")
def addition_advanced():
    return render_template("equation1.html", problem_type="addition", difficulty="advanced")


@app.route("/subtractionEasy")
def subtraction_easy():
    return render_template("equation1.html", problem_type="subtraction", difficulty="easy")


@app.route("/subtractionIntermediate")
def subtraction_intermediate():
    return render_template("equation1.html", problem_type="subtraction", difficulty="intermediate")


@app.route("/subtractionAdvanced")
def subtraction_advanced():
    return render_template("equation1.html", problem_type="subtraction", difficulty="advanced")


@app.route("/multiplicationEasy")
def multiplication_easy():
    return render_template("equation1.html", problem_type="multiplication", difficulty="easy")


@app.route("/multiplicationIntermediate")
def multiplication_intermediate():
    return render_template("equation1.html", problem_type="multiplication", difficulty="intermediate")


@app.route("/multiplicationAdvanced")
def multiplication_advanced():
    return render_template("equation1.html", problem_type="multiplication", difficulty="advanced")


if __name__ == "__main__":
    app.run(debug=True)

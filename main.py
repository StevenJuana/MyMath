from flask import Flask, redirect, url_for, render_template
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/lessons/")
def lessons():
    return render_template("lessons.html")


@app.route("/<problem_type>/<difficulty>/twoNumberProblem")
def two_number_problem(problem_type: str, difficulty: str):
    if difficulty == "Beginner":
        value1 = randint(0, 10)
        if problem_type == "Subtraction":
            value2 = randint(0, value1-1)
        else:
            value2 = randint(0, 10)

    elif difficulty == "Intermediate":
        value1 = randint(-25, 100)
        value2 = randint(-25, 100)

    else:
        value1 = randint(-300, 1000)
        value2 = randint(-300, 1000)

    answer = value1+value2 if problem_type == "Addition" else value1-value2 if problem_type == "Subtraction" \
        else value1*value2

    sign = "+" if problem_type == "Addition" else "-" if problem_type == "Subtraction" else "*"

    question_dict = {"value1": value1,
                     "value2": value2,
                     "answer": answer,
                     "sign": sign,
                     "heading": f"{problem_type} - {difficulty}",
                     "problem_type": problem_type}

    return render_template("twoNumEquation.html", question_dict=question_dict)


if __name__ == "__main__":
    app.run(debug=True)

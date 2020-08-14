from flask import Flask, redirect, url_for, render_template
from random import randint
from math import prod

app = Flask(__name__)


def subtract_list(lst: list):
    return lst[0] - sum(lst[1:])


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
        value2 = randint(0, value1 - 1) if problem_type == "Subtraction" else randint(0, 10)

    elif difficulty == "Intermediate":
        value1, value2 = randint(-25, 100), randint(-25, 100)

    else:
        value1, value2 = randint(-300, 1000), randint(-300, 1000)

    answer = value1 + value2 if problem_type == "Addition" else value1 - value2 if problem_type == "Subtraction" \
        else value1 * value2

    sign = "+" if problem_type == "Addition" else "-" if problem_type == "Subtraction" else "*"

    question_dict = {"value1": value1,
                     "value2": value2,
                     "answer": answer,
                     "sign": sign,
                     "heading": f"{problem_type} - {difficulty}",
                     "problem_type": problem_type}

    return render_template("twoNumEquation.html", question_dict=question_dict)


@app.route("/<problem_type>/<difficulty>/<num_numbers>")
def add_sub_mult_problem(problem_type: str, difficulty: str, num_numbers: int):
    if difficulty == "Beginner":
        values = [randint(0, 10) for x in range(num_numbers)]
    elif difficulty == "Intermediate":
        values = [randint(-25, 300) for x in range(num_numbers)]
    else:
        values = [randint(-300, 1000) for x in range(num_numbers)]

    answer = sum(values) if problem_type == "Addition" else subtract_list(values) if problem_type == "Subtraction" \
        else prod(values)

    sign = "+" if problem_type == "Addition" else "-" if problem_type == "Subtraction" else "*"

    question_dict = {"values": values,
                     "answer": answer,
                     "sign": sign,
                     "heading": f"{problem_type} - {difficulty}",
                     "problem_type": problem_type,
                     "difficulty": difficulty}

    return render_template("twoNumEquation.html", question_dict=question_dict) if num_numbers == 2 else \
        render_template("threeNumEquation.html", question_dict=question_dict) if num_numbers == 3 else \
        render_template("fourNumEquation.html", question_dict=question_dict)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, redirect, url_for, render_template
from random import randint
from math import prod

app = Flask(__name__)


def subtract_list(lst: list):
    return lst[0] - sum(lst[1:])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<problem_type>/<difficulty>/<num_numbers>")
def add_sub_mult_problem(problem_type: str, difficulty: str, num_numbers: str):
    if difficulty == "Beginner":
        values = sorted([randint(0, 10) for x in range(int(num_numbers))])
    elif difficulty == "Intermediate":
        values = [randint(-25, 300) for x in range(int(num_numbers))]
    else:
        values = [randint(-300, 1000) for x in range(int(num_numbers))]

    answer = sum(values) if problem_type == "Addition" else subtract_list(values) if problem_type == "Subtraction" \
        else prod(values)

    sign = "+" if problem_type == "Addition" else "-" if problem_type == "Subtraction" else "*"

    question_dict = {"values": values,
                     "answer": answer,
                     "sign": sign,
                     "heading": f"{problem_type} - {difficulty}",
                     "problem_type": problem_type,
                     "difficulty": difficulty}

    return render_template("twoNumEquation.html", question_dict=question_dict) if num_numbers == "2" else \
        render_template("threeNumEquation.html", question_dict=question_dict) if num_numbers == "3" else \
        render_template("fourNumEquation.html", question_dict=question_dict)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, redirect, url_for, render_template
from random import randint
from math import prod

app = Flask(__name__)


def subtract_list(lst: list):
    """Returns the result of subtracting all of the values in
    the given list"""
    return lst[0] - sum(lst[1:])


@app.route("/")
def home():
    """Takes user to the home page"""
    return render_template("index.html")


@app.route("/<problem_type>/<difficulty>/<num_numbers>")
def add_sub_mult_problem(problem_type: str, difficulty: str, num_numbers: str):
    """Generates an addition, subtraction or multiplication problem
    of 2,3 or 4 numbers. All relevant data about the question is sent to the
    appropriate HTML file where it is rendered and shown to the user."""

    # Generates the values that will be used in the problem. These values vary depending
    # on the difficulty of the question.
    if difficulty == "Beginner":
        values = sorted([randint(1, 10) for x in range(int(num_numbers))], reverse=True)
    elif difficulty == "Intermediate":
        values = [randint(-25, 300) for x in range(int(num_numbers))]
    else:
        values = [randint(-300, 1000) for x in range(int(num_numbers))]

    # Finds the answer for the question depending on if it is an addition, subtraction or
    # multiplication problem.
    answer = sum(values) if problem_type == "Addition" else subtract_list(values) \
        if problem_type == "Subtraction" else prod(values)

    # Sets the sign to a variable to use in the HTML file for formatting reasons
    sign = "+" if problem_type == "Addition" else "-" if problem_type == "Subtraction" else "*"

    # Store all information needed to be displayed in a dictionary which will be passed
    # to the HTML file to use
    question_dict = {"values": values,
                     "answer": answer,
                     "sign": sign,
                     "heading": f"{problem_type} - {difficulty}",
                     "problem_type": problem_type,
                     "difficulty": difficulty}

    # Render the appropriate HTML file depending on the number of numbers in the question
    return render_template("twoNumEquation.html", question_dict=question_dict) if num_numbers == "2" else \
        render_template("threeNumEquation.html", question_dict=question_dict) if num_numbers == "3" else \
        render_template("fourNumEquation.html", question_dict=question_dict)


if __name__ == "__main__":
    app.run(debug=True)

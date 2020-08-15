from flask import render_template, flash, request, session, Blueprint
from random import randint
import math

geometry = Blueprint("geometry", __name__, static_folder="static", template_folder="templates")


@geometry.route("/Geometry/<problem_type>", methods=['GET', 'POST'])
def area(problem_type):
    if problem_type == "triangle":
        base = randint(10, 15)
        height = randint(2, 8)
        answer = ((base * height) / 2)

        question_dict = dict(base=base, height=height, answer=answer, heading="Geometry - Area")
        session["currentDict"] = question_dict

        return render_template("triangle.html", question_dict=question_dict)

    elif problem_type == "circle":
        radius = randint(2, 10)
        answer = round(math.pi * (radius**2), 2)

        question_dict = dict(radius=radius, answer=answer, heading="Geometry - Area")
        session["currentDict"] = question_dict

        return render_template("circle.html", question_dict=question_dict)

    elif problem_type == "square":
        side = randint(2, 12)
        answer = side * side

        question_dict = dict(side=side, answer=answer, heading="Geometry - Area")
        session["currentDict"] = question_dict

        return render_template("square.html", question_dict=question_dict)

    elif problem_type == "rectangle":
        pass

from flask import render_template, flash, request, session, Blueprint
from random import randint

geometry = Blueprint("geometry", __name__, static_folder="static", template_folder="templates")


@geometry.route("/Geometry/<problem_type>", methods=['GET', 'POST'])
def area(problem_type):
    if problem_type == "triangle":
        base = randint(10, 15)
        height = randint(2, 8)
        answer = ((base * height) / 2)

        question_dict = dict(base=base, height=height, answer=answer, heading="Geometry - Triangle")
        session["currentDict"] = question_dict

        return render_template("triangle.html", question_dict=question_dict)

    elif problem_type == "circle":
        pass

    elif problem_type == "square":
        pass

    elif problem_type == "rectangle":
        pass

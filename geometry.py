from flask import render_template, flash, request, session, Blueprint
from random import randint

geometry = Blueprint("geometry", __name__, static_folder="static", template_folder="templates")


@geometry.route("/Geometry/<problem_type>")
def area(problem_type):
    def triangle():
        base = randint(10, 15)
        height = randint(2, 8)
        answer = ((base * height) / 2)

        question_dict = dict(base=base, height=height, answer=answer)
        session["currentDict"] = question_dict

        return render_template("triangle.html", question_dict)

    def circle():
        pass

    def square():
        pass

    def rectangle():
        pass

    return triangle() if problem_type == "triangle" else circle() if \
        problem_type == "circle" else square() if problem_type == \
        "square" else rectangle()

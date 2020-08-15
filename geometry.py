from flask import render_template, flash, request, session, Blueprint
from random import randint
import math

geometry = Blueprint("geometry", __name__, static_folder="static", template_folder="templates")


@geometry.route("/Geometry/Area/<problem_type>", methods=['GET', 'POST'])
def area(problem_type):
    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        # Check if a problem has been asked in this current session... if so, get its details
        if "currentDict" in session:
            question_dict = session["currentDict"]
            given_answer = request.form["answer"]

            # Check to see if the answer the user submitted is valid, then check its correctness and
            # give the appropriate error message
            if given_answer != None and given_answer != "":
                if given_answer.isnumeric() or (given_answer.count(".") == 1 and
                                                all([x.isnumeric() for x in given_answer.split(".")])):
                    if float(given_answer) == session["currentDict"]['answer']:
                        flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash('Invalid Answer, Please Submit a Number')
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        if session["currentDict"]["problem_type"] == "triangle":
            return render_template("triangle.html", question_dict=question_dict)
        elif session["currentDict"]["problem_type"] == "circle":
            return render_template("circle.html", question_dict=question_dict)
        elif session["currentDict"]["problem_type"] == "square":
            return render_template("square.html", question_dict=question_dict)
        else:
            return render_template("rectangle.html", question_dict=question_dict)

    else:
        if problem_type == "triangle":
            base = randint(10, 15)
            height = randint(2, 8)
            answer = ((base * height) / 2)

            question_dict = dict(base=base, height=height, answer=answer,
                                 heading="Geometry - Area", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("triangle.html", question_dict=question_dict)

        elif problem_type == "circle":
            radius = randint(2, 10)
            answer = round(math.pi * (radius**2), 2)

            question_dict = dict(radius=radius, answer=answer, heading="Geometry - Area", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("circle.html", question_dict=question_dict)

        elif problem_type == "square":
            side = randint(2, 12)
            answer = side * side

            question_dict = dict(side=side, answer=answer, heading="Geometry - Area", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("square.html", question_dict=question_dict)

        elif problem_type == "rectangle":
            width = randint(2, 5)
            length = randint(10, 15)
            answer = width * length

            question_dict = dict(width=width, length=length, answer=answer,
                                 heading="Geometry - Area", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("rectangle.html", question_dict=question_dict)


@geometry.route("/Geometry/Volume/<problem_type>", methods=['GET', 'POST'])
def volume(problem_type):
    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        # Check if a problem has been asked in this current session... if so, get its details
        if "currentDict" in session:
            question_dict = session["currentDict"]
            given_answer = request.form["answer"]

            # Check to see if the answer the user submitted is valid, then check its correctness and
            # give the appropriate error message
            if given_answer != None and given_answer != "":
                if given_answer.isnumeric() or (given_answer.count(".") == 1 and
                                                all([x.isnumeric() for x in given_answer.split(".")])):
                    if float(given_answer) == session["currentDict"]['answer']:
                        flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash('Invalid Answer, Please Submit a Number')
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        if session["currentDict"]["problem_type"] == "cube":
            return render_template("volumeCube.html", question_dict=question_dict)
        elif session["currentDict"]["problem_type"] == "pyramid":
            return render_template("volumePyramid.html", question_dict=question_dict)
        elif session["currentDict"]["problem_type"] == "cylinder":
            return render_template("volumeCylinder.html", question_dict=question_dict)
        else:
            return render_template("volumeSphere.html", question_dict=question_dict)

    else:
        if problem_type == "cube":
            side = randint(2, 10)
            answer = side * side * side

            question_dict = dict(side=side, answer=answer,
                                 heading="Geometry - Volume", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("volumeCube.html", question_dict=question_dict)

        elif problem_type == "pyramid":
            height = randint(7, 12)
            width = randint(3, 6)
            length = randint(9, 15)
            answer = round(((length * width * height) / 3), 2)

            question_dict = dict(height=height, width=width, length=length,
                                 answer=answer, heading="Geometry - Volume", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("volumePyramid.html", question_dict=question_dict)

        elif problem_type == "cylinder":
            radius = randint(2, 10)
            height = randint(10, 15)
            answer = round((height * math.pi * (radius ** 2)), 2)

            question_dict = dict(radius=radius, height=height, answer=answer,
                                 heading="Geometry - Volume", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("volumeCylinder.html", question_dict=question_dict)

        elif problem_type == "sphere":
            radius = randint(3, 10)
            answer = round(((4/3) * math.pi * (radius**3)), 2)

            question_dict = dict(radius=radius, answer=answer, heading="Geometry - Volume", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("volumeSphere.html", question_dict=question_dict)


@geometry.route("/Geometry/SurfaceArea/<problem_type>", methods=['GET', 'POST'])
def surface_area(problem_type):
    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        # Check if a problem has been asked in this current session... if so, get its details
        if "currentDict" in session:
            question_dict = session["currentDict"]
            given_answer = request.form["answer"]

            # Check to see if the answer the user submitted is valid, then check its correctness and
            # give the appropriate error message
            if given_answer != None and given_answer != "":
                if given_answer.isnumeric() or (given_answer.count(".") == 1 and
                                                all([x.isnumeric() for x in given_answer.split(".")])):
                    if float(given_answer) == session["currentDict"]['answer']:
                        flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash('Invalid Answer, Please Submit a Number')
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        if session["currentDict"]["problem_type"] == "cube":
            return render_template("surfaceAreaCube.html", question_dict=question_dict)
        elif session["currentDict"]["problem_type"] == "cone":
            return render_template("surfaceAreaCone.html", question_dict=question_dict)
        elif session["currentDict"]["problem_type"] == "cylinder":
            return render_template("surfaceAreaCylinder.html", question_dict=question_dict)
        else:
            return render_template("surfaceAreaSphere.html", question_dict=question_dict)

    else:
        if problem_type == "cube":
            side = randint(2, 10)
            answer = 6 * (side**2)

            question_dict = dict(side=side, answer=answer,
                                 heading="Geometry - Surfaces", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("surfaceAreaCube.html", question_dict=question_dict)

        elif problem_type == "cone":
            radius = randint(2, 7)
            height = randint(9, 15)
            answer = round(((math.pi * radius) * (radius + math.sqrt((height**2)*(radius**2)))), 2)

            question_dict = dict(radius=radius, height=height, answer=answer,
                                 heading="Geometry - Surfaces", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("surfaceAreaCone.html", question_dict=question_dict)

        elif problem_type == "cylinder":
            radius = randint(2, 10)
            height = randint(10, 15)
            answer = round(((2 * math.pi * radius * height) + (2 * math.pi * (radius**2))), 2)

            question_dict = dict(radius=radius, height=height, answer=answer,
                                 heading="Geometry - Surfaces", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("surfaceAreaCylinder.html", question_dict=question_dict)

        elif problem_type == "sphere":
            radius = randint(3, 10)
            answer = round((4 * math.pi * (radius**2)), 2)

            question_dict = dict(radius=radius, answer=answer, heading="Geometry - Volume", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("surfaceAreaSphere.html", question_dict=question_dict)

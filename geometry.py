# geometry.py

# This module contains all of the backend and routing for any geometry
# questions on MyMath. These include area, volume, surface area and
# circle properties

from flask import render_template, flash, request, session, Blueprint
from random import randint
import math

# Create a Blueprint for the "geometry.py" module
geometry = Blueprint("geometry", __name__, static_folder="static", template_folder="templates")


@geometry.route("/Geometry/Area/<problem_type>", methods=['GET', 'POST'])
def area(problem_type: str):
    """
     Generates a problem dealing with the area of either a triangle, circle,
     square, or rectangle.
    """
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
        # The parameter for this function (problem_type) is a string containing either
        # "triangle', 'circle', 'square', or 'rectangle' and is used to determine which
        # problem to generate

        if problem_type == "triangle":
            # Generate a base and height, use the area formula to calculate the answer
            base = randint(10, 15)
            height = randint(2, 8)
            answer = ((base * height) / 2)

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(base=base, height=height, answer=answer,
                                 heading="Geometry - Area", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("triangle.html", question_dict=question_dict)

        elif problem_type == "circle":
            # Generate a radius, use the area formula to calculate the answer
            radius = randint(2, 10)
            answer = round(math.pi * (radius**2), 2)

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(radius=radius, answer=answer, heading="Geometry - Area", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("circle.html", question_dict=question_dict)

        elif problem_type == "square":
            # Generate a side length, use the area formula to calculate the answer
            side = randint(2, 12)
            answer = side * side

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(side=side, answer=answer, heading="Geometry - Area", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("square.html", question_dict=question_dict)

        elif problem_type == "rectangle":
            # Generate a width and length, use the area formula to calculate the answer
            width = randint(2, 5)
            length = randint(10, 15)
            answer = width * length

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(width=width, length=length, answer=answer,
                                 heading="Geometry - Area", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("rectangle.html", question_dict=question_dict)


@geometry.route("/Geometry/Volume/<problem_type>", methods=['GET', 'POST'])
def volume(problem_type: str):
    """
     Generates a problem dealing with the volume of either a cube, pyramid,
     cylinder, or sphere.
    """
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
        # The parameter for this function (problem_type) is a string containing either
        # "cube', 'pyramid', 'cylinder', or 'sphere' and is used to determine which
        # problem to generate

        if problem_type == "cube":
            # Generate a side length, use the area formula to calculate the answer
            side = randint(2, 10)
            answer = side * side * side

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(side=side, answer=answer,
                                 heading="Geometry - Volume", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("volumeCube.html", question_dict=question_dict)

        elif problem_type == "pyramid":
            # Generate a height, width, and length use the area formula to calculate the answer
            height = randint(7, 12)
            width = randint(3, 6)
            length = randint(9, 15)
            answer = round(((length * width * height) / 3), 2)

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(height=height, width=width, length=length,
                                 answer=answer, heading="Geometry - Volume", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("volumePyramid.html", question_dict=question_dict)

        elif problem_type == "cylinder":
            # Generate a height, width, and length use the area formula to calculate the answer
            radius = randint(2, 10)
            height = randint(10, 15)
            answer = round((height * math.pi * (radius ** 2)), 2)

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(radius=radius, height=height, answer=answer,
                                 heading="Geometry - Volume", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("volumeCylinder.html", question_dict=question_dict)

        elif problem_type == "sphere":
            # Generate a radius use the area formula to calculate the answer
            radius = randint(3, 10)
            answer = round(((4/3) * math.pi * (radius**3)), 2)

            # Save all of the relevant information in a dictionary to pass through to the HTML file
            question_dict = dict(radius=radius, answer=answer, heading="Geometry - Volume", problem_type=problem_type)

            # Save this information in the session dictionary to reference once an answer is entered
            session["currentDict"] = question_dict

            # Render the appropriate HTML template to display the problem
            return render_template("volumeSphere.html", question_dict=question_dict)


@geometry.route("/Geometry/SurfaceArea/<problem_type>", methods=['GET', 'POST'])
def surface_area(problem_type: str):
    """
     Generates a problem dealing with the area of either a triangle, circle,
     square, or rectangle.
    """
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
        # The parameter for this function (problem_type) is a string containing either
        # "cube', 'cone', 'cylinder', or 'sphere' and is used to determine which
        # problem to generate.

        # For each problem, generate relevant measurement information, find the answer,
        # store important info in a dictionary (question_dict) to pass it to the HTML file
        # to use, store the question_dict in the session dictionary to reference later
        # to check answers, and then render the appropriate template

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
            answer = round(((math.pi * radius) * (radius + math.sqrt((height**2) + (radius**2)))), 2)

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

            question_dict = dict(radius=radius, answer=answer, heading="Geometry - Surfaces", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("surfaceAreaSphere.html", question_dict=question_dict)


@geometry.route("/Geometry/CircleProperties/<problem_type>", methods=['GET', 'POST'])
def circle_properties(problem_type):
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
        if session["currentDict"]["problem_type"] == "circumference":
            return render_template("circumference.html", question_dict=question_dict)
        else:
            return render_template("diameter.html", question_dict=question_dict)

    else:
        # The parameter for this function (problem_type) is a string containing either
        # "diameter' or 'circumference' and is used to determine which problem to generate

        # For each problem, generate relevant measurement information, find the answer,
        # store important info in a dictionary (question_dict) to pass it to the HTML file
        # to use, store the question_dict in the session dictionary to reference later
        # to check answers, and then render the appropriate template

        if problem_type == "diameter":
            radius = randint(2, 15)
            answer = radius * 2

            question_dict = dict(radius=radius, answer=answer,
                                 heading="Geometry - Circles", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("diameter.html", question_dict=question_dict)

        elif problem_type == "circumference":
            radius = randint(2, 10)
            answer = round((2 * radius * math.pi), 2)

            question_dict = dict(radius=radius, answer=answer,
                                 heading="Geometry - Circles", problem_type=problem_type)
            session["currentDict"] = question_dict

            return render_template("circumference.html", question_dict=question_dict)


# main.py

# This is the main file for the project. This file contains the logic to route
# to certain pages, as well as logic to generate and solve each problem.

from flask import Flask, redirect, url_for, render_template, flash, request, session
from random import randint
import calculations
from conversions import conversion_dict, conversion_types

# Dictionary that holds values used to generate problems
dv = dict(Beginner=[1, 10], Intermediate=[-25, 300], Advanced=[-300, 1000])

# Creates a flask app
app = Flask(__name__)

# Creates a secret key for the program
app.secret_key = "GarudaHacks4Ever"


def post_flash():
    """Checks the users answer and gives an appropriate message"""

    # Check if a problem has been asked in this current session... if so, get its details
    if "currentDict" in session:
        given_answer = request.form["answer"]

        # Check to see if the answer the user submitted is valid, then check its correctness and
        # give the appropriate error message
        if given_answer != None and given_answer != "":
            if given_answer.isnumeric() or (given_answer[0] == "-" and given_answer[1:].isnumeric()):
                if int(given_answer) == session["currentDict"]['answer']:
                    flash('Correct Answer!')
                else:
                    flash('Incorrect, try again')
            else:
                flash('Invalid Answer, Please Submit a Number')
        else:
            flash('Please Type Your Answer Above')


@app.route("/")
def home():
    """Takes user to the home page"""
    return render_template("index.html")


@app.route("/<problem_type>/<difficulty>/<num_numbers>", methods=['GET', 'POST'])
def add_sub_mult_problem(problem_type: str, difficulty: str, num_numbers: str):
    """Generates an addition, subtraction or multiplication problem
    of 2,3 or 4 numbers. All relevant data about the question is sent to the
    appropriate HTML file where it is rendered and shown to the user."""

    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        # Check if a problem has been asked in this current session... if so, get its details
        if "currentDict" in session:
            question_dict = session["currentDict"]
            given_answer = request.form["answer"]

            # Check to see if the answer the user submitted is valid, then check its correctness and
            # give the appropriate error message
            if given_answer != None and given_answer != "":
                if given_answer.isnumeric() or (given_answer[0] == "-" and given_answer[1:].isnumeric()):
                    if int(given_answer) == session["currentDict"]['answer']:
                        flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash('Invalid Answer, Please Submit a Number')
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        return render_template("twoNumEquation.html", question_dict=question_dict) if num_numbers == "2" else \
            render_template("threeNumEquation.html", question_dict=question_dict) if num_numbers == "3" else \
            render_template("fourNumEquation.html", question_dict=question_dict)

    else:
        # Generates the values that will be used in the problem. These values vary depending
        # on the difficulty of the question.
        values = sorted([randint(dv[difficulty][0], dv[difficulty][1]) for x in range(int(num_numbers))], reverse=True)

        # Finds the answer for the question
        answer = calculations.add_sub_mult_calc(values, problem_type)

        # Sets the sign to a variable to use in the HTML file for formatting reasons
        sign = "+" if problem_type == "Addition" else "-" if problem_type == "Subtraction" else "*"

        # Store all information needed to be displayed in a dictionary which will be passed
        # to the HTML file to use
        question_dict = dict(values=values, answer=answer, sign=sign, heading=f"{problem_type} - {difficulty}",
                             problem_type=problem_type, difficulty=difficulty, num_numbers=num_numbers)

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        # Render the appropriate HTML file depending on the number of numbers in the question
        return render_template("twoNumEquation.html", question_dict=question_dict) if num_numbers == "2" else \
            render_template("threeNumEquation.html", question_dict=question_dict) if num_numbers == "3" else \
            render_template("fourNumEquation.html", question_dict=question_dict)


@app.route("/Division/<difficulty>", methods=['GET', 'POST'])
def division_problem(difficulty: str):
    """Generates a division problem. All relevant data about the question is sent to the
    appropriate HTML file where it is rendered and shown to the user."""

    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        # Check if a problem has been asked in this current session... if so, get its details
        if "currentDict" in session:
            question_dict = session["currentDict"]

            given_quotient = request.form["quotient"]
            if question_dict["difficulty"] != "Beginner":
                given_remainder = request.form["remainder"]

            # Check to see if the answer the user submitted is valid, then check its correctness and
            # give the appropriate error message
            if given_quotient != None and given_quotient != "":
                if given_quotient.isnumeric():
                    if int(given_quotient) == session["currentDict"]["quotientAnswer"]:
                        if question_dict["difficulty"] != "Beginner":
                            if given_remainder is None or given_remainder == "":
                                flash('Please enter a remainder above')
                            else:
                                if given_remainder.isnumeric():
                                    if int(given_remainder) == session["currentDict"]["remainderAnswer"]:
                                        flash('Correct Answer!')
                                    else:
                                        flash('Incorrect, try again')
                                else:
                                    flash('Invalid Answer, Please Submit a Number')
                        else:
                            flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash('Invalid Answer, Please Submit a Number')
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        return render_template("divisionBeginner.html", question_dict=question_dict) if difficulty == "Beginner" \
            else render_template("divisionInterAdvanced.html", question_dict=question_dict)

    else:
        # Select the appropriate values for the problem based on the difficulty
        if difficulty == "Beginner":
            value1 = randint(10, 100)
            while calculations.is_prime(value1):
                value1 = randint(10, 100)
            potential_values = list(filter(lambda x : (value1 % x == 0), [x for x in range(1, value1)]))
            value2 = potential_values[randint(1, len(potential_values)-1)]

        else:
            value1 = randint(100, 999)
            value2 = randint(2, 9) if difficulty == "Intermediate" else randint(10, 99)

        # Calculate the quotient and remainder for the problem
        quotient = int(value1/value2)
        remainder = value1 % value2

        # Store all information needed to be displayed in a dictionary which will be passed
        # to the HTML file to use
        question_dict = dict(value1=value1, value2=value2, quotientAnswer=quotient, remainderAnswer=remainder, sign="/",
                             heading=f"Division - {difficulty}", difficulty=difficulty)

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        # Render the appropriate HTML file depending on the difficulty of the question
        return render_template("divisionBeginner.html", question_dict=question_dict) if difficulty == "Beginner" \
            else render_template("divisionInterAdvanced.html", question_dict=question_dict)


@app.route("/BasicAlgebra/SingleVariableEquation",  methods=['GET', 'POST'])
def basic_single_var():
    """Generates a single variable equation algebra problem. This can take a few forms:
    value1*x + value2 = value3, value1*x - value2 = value3, value1*x + value3 = -value2*x,
    or value1*x - value3 = value2*x"""

    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        # Check if a problem has been asked in this current session... if so, get its details
        if "currentDict" in session:
            question_dict = session["currentDict"]
            given_answer = request.form["answer"]

            # Check to see if the answer the user submitted is valid, then check its correctness and
            # give the appropriate error message
            if given_answer != None and given_answer != "":
                if given_answer.isnumeric() or (given_answer[0] == "-" and given_answer[1:].isnumeric()):
                    if int(given_answer) == session["currentDict"]["answer"]:
                        flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash('Invalid Answer, Please Submit a Number')
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        return render_template("algebraSingleVariable1.html", question_dict=question_dict) if \
            session["currentDict"]["problem_type"] in [0, 1] else \
            render_template("algebraSingleVariable2.html", question_dict=question_dict)

    else:
        problem_type = randint(0, 3)

        if problem_type in [0, 1]:
            value1 = randint(5, 99)

            while calculations.is_prime(value1):
                value1 = randint(5, 99)

            value2 = randint(5, 99) if problem_type == 0 else randint(5, value1 - 1)
            value3 = value1 + value2 if problem_type == 0 else value1 - value2

            potential_vars = list(filter(lambda x: (value1 % x == 0), [x for x in range(1, value1)]))
            answer = potential_vars[randint(0, len(potential_vars) - 1)]

            value1 = int(value1 / answer)
            sign = "+" if problem_type == 0 else "-"

        else:
            value1 = randint(2, 10)
            value2 = randint(1, 10) if problem_type == 2 else randint(1, value1 - 1)

            temp_combination = value1 + value2 if problem_type == 2 else value1 - value2

            answer = randint(1, 10)

            value2 = -value2 if problem_type == 2 else value2
            value3 = answer * temp_combination if problem_type == 2 else -answer * temp_combination
            answer = -answer if problem_type == 2 else answer

            sign = "+" if problem_type == 2 else "-"
            value3 = abs(value3)

        potential_vars = ["x", "y", "z"]
        variable = potential_vars[randint(0, len(potential_vars)-1)]

        question_dict = dict(value1=value1, value2=value2, value3=value3, answer=answer, sign=sign,
                             heading=f"Algebra -\nSingle Variable", variable=variable, problem_type=problem_type)

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        return render_template("algebraSingleVariable1.html", question_dict=question_dict) if problem_type in [0, 1] \
            else render_template("algebraSingleVariable2.html", question_dict=question_dict)


@app.route("/BasicAlgebra/Inequalities", methods=['GET', 'POST'])
def inequalities():
    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        # Check if a problem has been asked in this current session... if so, get its details
        if "currentDict" in session:
            question_dict = session["currentDict"]
            given_answer = request.form["answer"]

            # Check to see if the answer the user submitted is valid, then check its correctness and
            # give the appropriate error message
            if given_answer != None and given_answer != "":
                if not given_answer.isnumeric():
                    if given_answer == session["currentDict"]["answer"]:
                        flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash("Invalid Answer, Please Enter Either '>', '<', or '='")
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        return render_template("algebraInequalities.html", question_dict=question_dict)

    else:
        value1 = randint(0, 1000)
        value2 = randint(0, 1000)
        answer = ">" if value1 > value2 else "<" if value1 < value2 else "="

        question_dict = dict(value1=value1, value2=value2, answer=answer, heading="Algebra - Inequalities")

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        return render_template("algebraInequalities.html", question_dict=question_dict)


@app.route("/BasicAlgebra/Units", methods=['GET', 'POST'])
def convert_units():
    # If the user has just entered an answer submission, check the validity and correctness
    if request.method == 'POST':
        question_dict = session["currentDict"]
        
        post_flash()

        # Render the template show the screen shows the correct values
        return render_template("algebraConversions.html", question_dict=question_dict)

    else:
        type_units = list(conversion_types.keys())[randint(0, 2)]

        unit1 = conversion_types[type_units][randint(0, 3)]

        unit2 = conversion_types[type_units][randint(0, 3)]
        while unit2 == unit1:
            unit2 = conversion_types[type_units][randint(0, 3)]

        if unit1 == "feet" or unit1 == "inch":
            amt_unit1 = randint(1000, 2000)
        elif unit1 == "gram":
            amt_unit1 = randint(500, 1000)
        elif unit1 == "kilometers":
            amt_unit1 = randint(2, 5)
        else:
            amt_unit1 = randint(50, 100)

        answer = round(amt_unit1 * conversion_dict[unit1][unit2], 2)

        question_dict = dict(unit1=unit1, unit2=unit2, amt_unit1=amt_unit1, answer=answer,
                             heading="Algebra - Unit Conversion")

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        return render_template("algebraConversions.html", question_dict=question_dict)


if __name__ == "__main__":
    app.run(debug=True)

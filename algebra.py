from flask import render_template, flash, request, session, Blueprint
from random import randint
from conversions import conversion_dict, conversion_types
import calculations

algebra = Blueprint("algebra", __name__, static_folder="static", template_folder="templates")


@algebra.route("/BasicAlgebra/SingleVariableEquation", methods=['GET', 'POST'])
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
        variable = potential_vars[randint(0, len(potential_vars) - 1)]

        question_dict = dict(value1=value1, value2=value2, value3=value3, answer=answer, sign=sign,
                             heading=f"Algebra -\nSingle Variable", variable=variable, problem_type=problem_type)

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        return render_template("algebraSingleVariable1.html", question_dict=question_dict) if problem_type in [0, 1] \
            else render_template("algebraSingleVariable2.html", question_dict=question_dict)


@algebra.route("/BasicAlgebra/Inequalities", methods=['GET', 'POST'])
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


@algebra.route("/BasicAlgebra/Units", methods=['GET', 'POST'])
def convert_units():
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


@algebra.route("/BasicAlgebra/ExponentsAndLogarithms")
def exponents_logs():
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
        return render_template("exponent1.html", question_dict=question_dict) if \
            session["currentDict"]["question_type"] == 0 else \
            render_template("exponent2.html", question_dict=question_dict) if \
            session["currentDict"]["question_type"] == 1 else \
            render_template("logarithm.html", question_dict=question_dict)

    else:
        question_type = randint(0, 2)

        if question_type == 0:
            value1, value2 = randint(1, 10), randint(1, 3)
            answer = value1 ** value2

        elif question_type == 1:
            value1, answer = randint(1, 10), randint(1, 3)
            value2 = value1 ** answer

        else:
            value1, answer = randint(2, 10), randint(2, 15)

        question_dict = dict(value1=value1, value2=value2, answer=answer, heading="Algebra - Exponents and Logarithms",
                             question_type=question_type) if question_type in [0, 1] \
                        else dict(value1=value1, answer=answer, question_type=question_type)

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        return render_template("exponent1.html", question_dict=question_dict) if \
            question_type == 0 else render_template("exponent2.html", question_dict=question_dict) \
            if question_type == 1 else render_template("logarithm.html", question_dict=question_dict)

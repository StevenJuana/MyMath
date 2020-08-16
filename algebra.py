# algebra.py

# This module contains all of the backend and routing for any algebra
# questions on MyMath. These include single variable equations,
# inequalities, unit conversions and exponents/logarithms


from flask import render_template, flash, request, session, Blueprint
from random import randint
from conversions import conversion_dict, conversion_types
import calculations

# Create a Blueprint for the "algebra.py" module
algebra = Blueprint("algebra", __name__, static_folder="static", template_folder="templates")


@algebra.route("/BasicAlgebra/SingleVariableEquation", methods=['GET', 'POST'])
def basic_single_var():
    """
    Generates a single variable equation algebra problem. This can take a few forms:
    value1*x + value2 = value3, value1*x - value2 = value3, value1*x + value3 = -value2*x,
    or value1*x - value3 = value2*x
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
        # Choose a random integer 0-3, which will decide which type of algebra problem we generate
        problem_type = randint(0, 3)

        # The first two types of problems are in the form of value1*x (+ or -) value2 = value3
        if problem_type in [0, 1]:
            # Choose a random integer between 5-99 to be the first value
            value1 = randint(5, 99)

            # Ensure that the number is prime so we can use it to create a variable
            while calculations.is_prime(value1):
                value1 = randint(5, 99)

            # If we are doing an addition with a variable, set it between 5-99, but if we are
            # performing a subtraction, ensure the value is less than the first value to make
            # it a clean subtraction
            value2 = randint(5, 99) if problem_type == 0 else randint(5, value1 - 1)

            # Add the numbers if it is addition problem, subtract them if it is a subtraction problem
            value3 = value1 + value2 if problem_type == 0 else value1 - value2

            # We create the variable (which is the answer to the question) by finding all values that
            # cleanly divide our first value, and then choosing a random one as our variable for the
            # question
            potential_vars = list(filter(lambda x: (value1 % x == 0), [x for x in range(1, value1)]))
            answer = potential_vars[randint(0, len(potential_vars) - 1)]

            # Change the value of value1 to be value1 divided by the variable such that the variable
            # multiplied by the new value1 will make the initial equation correct
            value1 = int(value1 / answer)

            # Save the sign of the problem to pass through to the HTML file for formatting
            sign = "+" if problem_type == 0 else "-"

        else:
            # These next two problem types are in the form of value1*x +or- value3 = +or-value2*x

            # Set up the two values, with the second one either being random if it is an addition
            # problem or less than the value1 if it is a subtraction problem
            value1 = randint(2, 10)
            value2 = randint(1, 10) if problem_type == 2 else randint(1, value1 - 1)

            # Store either the sum or subtraction of the two values to use later in calculations
            temp_combination = value1 + value2 if problem_type == 2 else value1 - value2

            # Create the answer to the question, this will be the variable. We create it now so
            # we can, in a sense, reverse-engineer the question so there will always be a clean
            # answer
            answer = randint(1, 10)

            # Adjust the signs and create our value3, all of which are dependent on the type of
            # form of the question
            value2 = -value2 if problem_type == 2 else value2
            value3 = answer * temp_combination if problem_type == 2 else -answer * temp_combination
            answer = -answer if problem_type == 2 else answer

            # Save the sign to pass it on to the HTML file for formatting
            sign = "+" if problem_type == 2 else "-"

            # Adjust the value3 such that it shows correctly on the webpage
            value3 = abs(value3)

        # This chooses which variable is used in the question
        potential_vars = ["x", "y", "z"]
        variable = potential_vars[randint(0, len(potential_vars) - 1)]

        # Save all of the relevant information in a dictionary to pass through to the HTML file
        question_dict = dict(value1=value1, value2=value2, value3=value3, answer=answer, sign=sign,
                             heading=f"Algebra - Variables", variable=variable, problem_type=problem_type)

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        # Render the appropriate HTML template to display the problem
        return render_template("algebraSingleVariable1.html", question_dict=question_dict) if problem_type in [0, 1] \
            else render_template("algebraSingleVariable2.html", question_dict=question_dict)


@algebra.route("/BasicAlgebra/Inequalities", methods=['GET', 'POST'])
def inequalities():
    """
     Generates a problem that deals with inequalities between two numbers in
     the form of x > y, or x < y, or x = y.
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
        # Choose two random integers between 1 and 1000 to compare
        value1 = randint(1, 1000)
        value2 = randint(1, 1000)

        # Compare value1 on the left and value2 on the right and store the answer
        answer = ">" if value1 > value2 else "<" if value1 < value2 else "="

        # Save all of the relevant information in a dictionary to pass through to the HTML file
        question_dict = dict(value1=value1, value2=value2, answer=answer, heading="Algebra - Inequalities")

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        # Render the appropriate HTML template to display the problem
        return render_template("algebraInequalities.html", question_dict=question_dict)


@algebra.route("/BasicAlgebra/Units", methods=['GET', 'POST'])
def convert_units():
    """
    Generates a problem that deals with converting one type of units to another.
    This can come in three categories: weight, length and volume. The relevant
    information to perform these conversions is stored in the file "conversions.py"
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
        return render_template("algebraConversions.html", question_dict=question_dict)

    else:
        # Select a type of units to convert from (weight, length, volume)
        type_units = list(conversion_types.keys())[randint(0, 2)]

        # Select a unit from the list of 4
        unit1 = conversion_types[type_units][randint(0, 3)]

        # Select a unit to convert to, and ensure that it is not the same as unit1
        unit2 = conversion_types[type_units][randint(0, 3)]
        while unit2 == unit1:
            unit2 = conversion_types[type_units][randint(0, 3)]

        # Select the amount of the first unit (unit1) to convert to the second
        if unit1 == "feet" or unit1 == "inch":
            amt_unit1 = randint(1000, 2000)
        elif unit1 == "gram":
            amt_unit1 = randint(500, 1000)
        elif unit1 == "kilometers":
            amt_unit1 = randint(2, 5)
        else:
            amt_unit1 = randint(50, 100)

        # Calculate the conversion using the conversion dictionary from "conversions.py"
        answer = round(amt_unit1 * conversion_dict[unit1][unit2], 2)

        # Save all of the relevant information in a dictionary to pass through to the HTML file
        question_dict = dict(unit1=unit1, unit2=unit2, amt_unit1=amt_unit1, answer=answer,
                             heading="Algebra - Units")

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        # Render the appropriate HTML template to display the problem
        return render_template("algebraConversions.html", question_dict=question_dict)


@algebra.route("/BasicAlgebra/ExponentsAndLogarithms", methods=['GET', 'POST'])
def exponents_logs():
    """
    Generates a problem dealing with either exponents or logarithms in the form of
    value1**x = value2, value1**value2 = x, logbasevalue1(value1**x) = x
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
                if given_answer.isnumeric():
                    if int(given_answer) == session["currentDict"]["answer"]:
                        flash('Correct Answer!')
                    else:
                        flash('Incorrect, try again')
                else:
                    flash('Invalid Answer, Please Submit a Number')
            else:
                flash('Please Type Your Answer Above')

        # Render the template show the screen shows the correct values
        return render_template("exponent1.html", question_dict=question_dict) if \
            session["currentDict"]["question_type"] == 0 else \
            render_template("exponent2.html", question_dict=question_dict) if \
            session["currentDict"]["question_type"] == 1 else \
            render_template("logarithm.html", question_dict=question_dict)

    else:
        # Choose a question type, where 0-1 is exponent questions and 2 is a log question
        question_type = randint(0, 2)

        # Set up the values for an exponent question, just random numbers
        if question_type == 0:
            value1, value2 = randint(1, 10), randint(1, 3)
            answer = value1 ** value2

        elif question_type == 1:
            value1, answer = randint(1, 10), randint(1, 3)
            value2 = value1 ** answer

        # Set up the values for a logarithm question, just random numbers
        else:
            value1, answer = randint(2, 10), randint(2, 15)

        # Save all of the relevant information in a dictionary to pass through to the HTML file
        question_dict = dict(value1=value1, value2=value2, answer=answer, heading="Algebra - Exp/Logs",
                             question_type=question_type) if question_type in [0, 1] else \
                        dict(value1=value1, answer=answer, heading="Algebra - Exp/Logs", question_type=question_type)

        # Save this information in the session dictionary to reference once an answer is entered
        session["currentDict"] = question_dict

        # Render the appropriate HTML template to display the problem
        return render_template("exponent1.html", question_dict=question_dict) if \
            question_type == 0 else render_template("exponent2.html", question_dict=question_dict) \
            if question_type == 1 else render_template("logarithm.html", question_dict=question_dict)

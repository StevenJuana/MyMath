# division.py

# This module contains all of the backend and routing for the
# division problems for the program

from flask import render_template, flash, request, session, Blueprint
from random import randint
import calculations

# Create a Blueprint for the "division.py" module
division = Blueprint("division", __name__, static_folder="static", template_folder="templates")


@division.route("/Division/<difficulty>", methods=['GET', 'POST'])
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
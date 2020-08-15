from flask import render_template, flash, request, session, Blueprint
from random import randint
import calculations

addSubMult = Blueprint("addSubMult", __name__, static_folder="static", template_folder="templates")


# Dictionary that holds values used to generate problems
dv = dict(Beginner=[1, 10], Intermediate=[-25, 300], Advanced=[-300, 1000])


@addSubMult.route("/<problem_type>/<difficulty>/<num_numbers>", methods=['GET', 'POST'])
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
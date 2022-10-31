"""
Purpose: This program helps users practice their multiplication tables. It starts
		 by asking the user to enter a starting factor (from 2-12) and then it
		 randomly generates multiplication problems until the user answers 3 in
		 a row correctly. When this happens, the program displays a score report
		 and (encouraging) message for the user to let them know how they did.
Author: Mr. Bloom
Date: Fall 2018
"""

import random

def question(factor):
	"""
	Purpose: Creates a multiplication problem and asks the user to answer it.
	Parameters: Takes a factor (integer) to be used in the multiplication problem.
	Return Val: Returns a string indicating whether their answer was correct or not.
	"""
	print("------------------------")
	result = ""

	num = random.randrange(2,13)        # create random multiplication problem

	answer = int(input("%d x %d? " % (factor, num)))    # ask question and get answer
	correctAnswer = factor * num

	if answer == correctAnswer:         # user answer is correct
		result += "Correct!"
	else:                               # user answer is incorrect
		result += "Nope. %d x %d = %d" % (factor, num, correctAnswer)

	return result                       # return result (and answer if got wrong)


def getFactor():
	"""
	Purpose: To get a number (in range 2 thru 12) from the user.
	Parameters: None.
	Return Val: Returns a factor (integer) to be used in multiplication problems.
	"""
	while True:
		factor = int(input("What factor would you like to work on? "))
		if factor >= 2 and factor <= 12:
			return factor
		print("Please choose a starting factor from 2-12.")


def scoreReport(correct, total):
	"""
	Purpose: To display a score report and provide feedback to the user.
	Parameters: Takes 2 integers, the number of problems answered correctly and
				the number of total problems/questions asked, respectively.
	Return Val: None.
	"""

	answerSummary = "You got %d out of %d correct. " % (correct, total)
	percentCorrect = (float(correct) / total) * 100

	# varies output message at end depending on percentage correct
	if percentCorrect >= 90:
		answerSummary += "Excellent work!"
	elif percentCorrect >= 80:
		answerSummary += "Good work!"
	elif percentCorrect >= 70:
		answerSummary += "You could use some practice."
	else:
		answerSummary += "Uh oh..."

	print(answerSummary)


def main():
	print("Welcome to MathQuiz v0.1!\n")

	factor = getFactor()

	correctInARow = 0                   # keep track of correct consecutive answers
	totalCorrect = 0                    # keep track of correct answers
	totalProblems = 0                   # keep track of number of problems

	# keep asking questions until user gets 3 in a row correct
	while correctInARow < 3:
		result = question(factor)       # ask multiplication problem
		totalProblems += 1              # update total number of problems

		print(result)                   # display result (correct/incorrect)

		if result == "Correct!":
			correctInARow += 1          # update correct consecutive answers
			totalCorrect += 1           # update total number of correct answers
		else:
			correctInARow = 0           # reset when user answers one incorrectly

	scoreReport(totalCorrect, totalProblems)


main()

"""
	Description: This program gets the name of a python file from its user,
				 goes through the file line by line, and determines whether
				 there are any lines that contain unbalanced parentheses.
	Author: Jonas Pfefferman
	Date: 9/29/2022
"""

#------------------------------------------------------------------------------#
def isBalancedHelper(line, count):
	""" Recursively examine the characters in the string from left to right,
		while keeping track of how many open parentheses have not yet been closed.
		If unclosed paren counter ever becomes negative, you have unbalanced parens.
	"""
	# your recursive code goes here
	print(line, count)
	if len(line) <= 1 and count == 0:
		return True
	elif len(line) <= 1 and count 1= 0:
		return False
	if line[0] == "(":
		print("+")
		count += 1
	elif line[0] == ")":
		print("-")
		count -= 1
	return isBalancedHelper(line[1:], count)

#------------------------------------------------------------------------------#
def isBalanced(line):
	"""
	Purpose: determine if a single line from the file has balanced parentheses
	Parameters: a line from the file (string)
	Return Val: a boolean indicating whether the line has balanced parens
	"""
	# set initial unclosed parens count to 0 & delegate work to recursive function
	return isBalancedHelper(line, 0)

#------------------------------------------------------------------------------#
def main():

	# get the name of a python file from its user
	fileName = input("file name: ")

	errorLines = []
	# read file line by line and determine whether there are any w/ unbalanced parens
	checkFile = open(fileName, 'r')
	for line in checkFile:
		print(line)
		if isBalanced(line) == False:
			errorLines.append(line)
	print(errorLines)





main()

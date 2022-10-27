"""
Description: This program takes in a string and a number and recursively copies
			 each charcater of the string the given number of times.
Date: 9/19/22
Author: Jonas Pfefferman '24
"""

def getInt(prompt, minVal, maxVal):
	"""
	Purpose: Checks to see if the user-input matches with the minimum and maximum
			 value allowed for each field
	Parameters: Question prompt (string), minimum value (integer), maximum value
				(integer)
	Return Value: The user's step goal (integer), window width (integer),
				   window height (integer)
	"""

	userInput = inputInteger(prompt)
	while True:
		if minVal <= userInput and maxVal >= userInput:
			return userInput
		else:
			print("\nInvalid entry: Must be between %i and %i" % (minVal, maxVal))
			userInput = inputInteger(prompt)

def inputInteger(prompt):
	"""
	Purpose: Asks for the user's input then runs a try/except to see if it works
			 as an integer
	Parameters: Question prompt (string)
	Return Value: User-input in the correct data type (integer)
	"""
	while True:
		inputInteger = input(prompt)
		try:
			intInput = int(inputInteger)
			return intInput
		except ValueError:
			print("\nThat is not a valid integer.")

def repeatChar(strInput, num):
	"""
	Description: Function recursively copies a specific character within an
				 ever-shrinking string
	Parameters: The string (str) and the number of times to copy each character (int)
	Returns: String of all the copied characters
	"""

	if num == 0:
		return strInput
	else:
		# once the string is down to one character or less, function is done copying
		if len(strInput) <= 1:
			return strInput * num # if the string is already one character, make sure to clone it
		else:
			return strInput[0] * num + repeatChar(strInput[1:], num) # send back the next characters to be copied


#------------------------------------------------------------------------------#

def main():

	# getting user inputs
	strInput = input("string: ")
	promptStr = "number of times to repeat each character: "
	num = getInt(promptStr, 0, 10000000000)

	repeatedString = repeatChar(strInput, num)
	print("\n" + repeatedString)



main()

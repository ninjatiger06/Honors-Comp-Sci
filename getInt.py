def getInt(prompt, minVal, maxVal):
	"""
	Purpose: Checks to see if the user-input matches with the minimum and maximum
			 value allowed for each field
	Parameters: Question prompt asking for user's input (string), minimum value
				(integer), maximum value (integer)
	Return Value: The user's step goal (integer), window width (integer),
				   window height (integer)
	"""

	userInput = inputInteger(prompt)
	while True:
		if minVal <= userInput <= maxVal:
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

#------------------------------------------------------------------------------#

def main():
	userInt = getInt("test prompt", 0, 100)

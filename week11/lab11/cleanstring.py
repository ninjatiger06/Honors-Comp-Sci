"""
Description: This program recursively searches through a user-inputted string
			 and removes all occurences of a speciic character
Date: 9/19/22
Author: Jonas Pfefferman '24
"""

def getChar():
	"""
		Description: Makes sure that the user inputs only a single character
		Parameters: None
		Returns: User's inputted character (string)
	"""
	ch = input("ch: ").lower()
	while len(ch) != 1:
		print("\nInvalid. Please enter a single character")
		ch = input("ch: ")

	return ch

def removeChar(strInput, ch):
	"""
		Description: Takes in a string and removes the first instance of a
					 specific character
		Parameters: String to clean (str) and character to remove (str)
		Returns: The string with the first instance of the character removed
	"""

	if len(strInput) < 1:
		return strInput
	else:
		if strInput[0].lower() == ch:
			return removeChar(strInput[1:], ch)
		else:
			return strInput[0] + removeChar(strInput[1:], ch)
		# if the first character is the one to remove, its value will become 0 (false)
		return strInput[0] * (strInput[0] != ch) + removeChar(strInput[1:], ch)


def main():

	strInput = input("string: ")
	ch = getChar()

	cleanedString = removeChar(strInput, ch)
	print("\n" + cleanedString)


main()

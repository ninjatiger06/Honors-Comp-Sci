"""
Description: This program recursively searches through a user-inputted string
			 and removes all occurences of a speciic character
Date: 9/19/22
Author: Jonas Pfefferman '24
"""

def getChar(prompt):
	"""
		Description: Makes sure that the user inputs only a single character
		Parameters: Prompt to give the user to request their input (string)
		Returns: User's inputted character (string)
	"""
	while True:
		ch = input(prompt).lower()
		if len(ch) == 1:
			return ch
		else:
			print("\nInvalid. Please enter a single character")

	return ch

def removeChar(text, ch):
	"""
		Description: Takes in a string and removes the first instance of a
					 specific character
		Parameters: String to clean (str) and character to remove (str)
		Returns: The string with the first instance of the character removed
	"""

	if len(text) < 1:
		return text
	else:
		if text[0] == ch:
			return removeChar(text[1:], ch)
		else:
			return text[0] + removeChar(text[1:], ch)


def main():

	text = input("string: ")
	prompt = "ch: "
	ch = getChar(prompt)

	cleanedString = removeChar(text, ch)
	print("\n%s" % (cleanedString))


main()

"""
Description: This program recursively searches through a user-inputted string
			 and removes all occurences of a speciic character
Date: 9/19/22
Author: Jonas Pfefferman '24
"""
def removeChar(str, ch):
	"""
		Description: Takes in a string and removes the first instance of a
					 specific character
		Parameters: String to clean (str) and character to remove (str)
		Returns: The string with the first instance of the character removed
	"""

	if len(str) <= 1:
		return str
	else:
		# if the first character is the one to remove, its value will become 0 (false)
		return str[0] * (str[0] != ch) + removeChar(str[1:], ch)


def main():

	str = input("string: ").lower()
	ch = input("ch: ").lower()
	while len(ch) != 1:
		print("\nInvalid. Please enter a single character")
		ch = input("ch: ")

	print(removeChar(str, ch))


main()

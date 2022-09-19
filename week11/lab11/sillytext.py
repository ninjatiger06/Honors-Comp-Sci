"""
Description: This program takes in a string and a number and recursively copies
			 each charcater of the string the given number of times.
Date: 9/19/22
Author: Jonas Pfefferman '24
"""

def sillyfy(str, num):
	"""
	Description: Function recursively copies a specific character within an
				 ever-shrinking string
	Parameters: The string and the number of times to copy each character
	Returns: String of all the copied characters
	"""

	# once the string is down to one character or less, function is done copying
	if len(str) <= 1:
		return str * num # if the string is already one character, make sure to clone it
	else:
		return str[0] * num + sillyfy(str[1:], num) # send back the next characters to be copied


#------------------------------------------------------------------------------#

def main():

	# getting user inputs
	str = input("string: ")
	num = int(input("num: "))

	print(sillyfy(str, num))



main()

"""
Description: This program recursively searches through a user-inputted string
			 and removes all occurences of a speciic character
Date: 9/19/22
Author: Jonas Pfefferman '24
"""

def main():

	str = input("string: ")
	ch = input("ch: ")
	while len(ch) != 1:
		print("\nInvalid. Please enter a single character")
		ch = input("ch: ")


main()

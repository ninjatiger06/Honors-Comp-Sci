def isDigit_iterative(S):
	""" Iterative function to verify if string is a number """
	count = 0
	for char in S:
		if char >= '0' and char <= '9':
			count += 1

	if count == len(S):
		return True
	else:
		return False


def isDigit_recursive(S):
	""" Recursive function to verify if string is a number """
	if S == "":
		return S
	else:
		if S[-1] >= '0' and S[-1] <= '9':
			return isDigit_recursive(S[:len(S)])


def isPalindrome_iterative(S):
	""" An iterative function to check whether or not a word is a palindrome """
	wordLen = len(S)
	for i in range(0, wordLen/2):       # traverse to the middle character in the word
		beginChar = S[i]                # get 1st, 2nd, 3rd charaters...
		endChar = S[wordLen-i-1]        # get last, second-to-last, third-to-last chars
		if beginChar != endChar:        # check if opposite characters are the same
			return False                # if they're not, then word is not a palindrome
	return True


def isPalindrome_recursive(S):
	""" A recursive function to check whether or not a word is a palindrome """
	pass


def main():
	numText = str(input("Enter a number: "))

	if isDigit_iterative(numText) == True:
		print("User entered a number!")
	else:
		print("User did NOT enter a number!")

	if isDigit_recursive(numText) == True:
		print("User entered a number!")
	else:
		print("User did NOT enter a number!")

	if numText.isdigit() == True:
		print("User entered a number!")
	else:
		print("User did NOT enter a number!")


	text = str(input("Enter a string: "))

	if isPalindrome_iterative(text) == True:
		print("String is a palindrome!")
	else:
		print("String is NOT a palindrome!")

	if isPalindrome_recursive(text) == True:
		print("String is a palindrome!")
	else:
		print("String is NOT a palindrome!")


main()

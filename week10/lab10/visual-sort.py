def printIntro():
	"""
		Purpose: Prints introductory spiel to explain how sorting works
		Parameters: None
		Return Val: None
	"""
	print("Welcome to visual-sort.py")
	print("This program is going to visualize the selection sorting algorithm")
	print("Selection sort works by finding the smallest item in a list, moving it to position 0, moving everything else up, and repeating the process\n")
	print("The smallest index starts as the current position plus 1 because everything before the current position has already been sorted")
	print("Everything to the right is then checked. If a smaller value is found, it's moved to [0]. If not, the 'marker' of what's sorted moves one over to the right\n\n")
	return

def makeList(N):
	"""
		Purpose: Makes a numbered list of an inputted length
		Parameters: Length of the list (integer)
		Return Val: A list of numbers
	"""
	L = []
	# create the list of numbers up to the given number
	for i in range(N):
		L.append(i)
	return L

def selectionSort(L):
	"""
		Purpose: Sorts a given list and prints out the steps to sorting
		Parameters: An unsorted list (list of integers)
		Return Val: None
	"""
	# the maximum number of times the list can have something to sort is the
		# length of the list - 1
	for i in range(len(L)-1):
		print("Current list arrangement: ", L)

		# the smallest number is automatically the first index in the "unsorted" list
		minIdx = i + 1
		print("The current smallest value is %i at index %i\n" % (L[minIdx], minIdx))

		# iterate through the unsorted list
		for j in range(i, len(L)):
			print("\n" + "-" * L[minIdx], "[%i] <-- minimum" % (L[minIdx]))
			print("-" * L[j], "[%i]" % (L[j]))
			print("Current Value (%i) < Minimum Value (%i): %r" % (L[j], L[minIdx], L[j] < L[minIdx]))
			# check if the value at the current index is smaller than the current
				# smallest value
			if L[j] < L[minIdx]:
				print("%i at index %i is smaller than %i, so it become the new smallest value"
						% (L[j], j, L[minIdx]))
				# if it is, the current index becomes the index of the smallest value
				minIdx = j
		print("The smallest value is %i and index %i" %(L[minIdx], minIdx))

		# swap the places of the smallest value and position 0 of the unsorted list
		L[i], L[minIdx] = L[minIdx], L[i]

		# all the prints!
		print("Now the smallest value swaps places with the value at index 0 of the unsorted list\n", L, "\n")

		# scuffed keydown because I don't want to re-learn it right now
		input("Press enter to continue... ")
		print("\n\n")
	print("No more swaps left, so the sort is complete")

	return

def main():
	from random import shuffle

	printIntro()

	# Get how long the list should be from the user
	N = int(input("Length of list (N): "))
	L = makeList(N)
	shuffle(L)
	selectionSort(L)


main()

def printIntro():
	"""
		Purpose: Prints introductory spiel to explain how sorting works
		Parameters: None
		Returns: None
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
		Returns: A list of numbers
	"""
	L = []
	for i in range(N):
		L.append(i)
	return L

def selectionSort(L):
	"""
		Purpose: Sorts a given list and prints out the steps to sorting
		Parameters: An unsorted list (list of integers)
		Returns: None
	"""
	for i in range(len(L)-1):
		print("Current list arrangement: ", L)
		minIdx = i + 1
		# print("The minimum index is currently: %i, and the value at that index is %i" % (minIdx, L[minIdx]))
		for j in range(i, len(L)):
			# print("\tWithin the small list, at index %i with value %i" % (j, L[j]))
			# print("\tIs the current value less than the set minimum value? (T/F)", L[j] < L[minIdx])
			if L[j] < L[minIdx]:
				# print("\t\tIt is smaller, so the new smallest number is now at index %i with a value of %i" % (minIdx, L[minIdx]))
				minIdx = j
		print("The smallest value is %i and index %i" %(L[minIdx], minIdx))
		# print("Now put the smallest value at the beginning of the unsorted list")
		L[i], L[minIdx] = L[minIdx], L[i]
		print("Now the smallest value swaps places with the value at index 0 of the unsorted list\n", L, "\n\n")
	print("No more swaps left, so the sort is complete")

	return

def main():
	from random import shuffle

	printIntro()
	N = int(input("Length of list (N): "))
	L = makeList(N)
	shuffle(L)
	selectionSort(L)


main()

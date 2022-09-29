from random import shuffle

"""                       INSTRUCTIONS
		When you get this up and running, copy-paste your merge() and
		mergeSort() functions into your sorts.py file.
		This way, all of your sorting algorithms will be in one place.
"""

def makeList(N):
	L = []
	for i in range(N):
		L.append(i)
	return L


def merge(leftL, rightL, L):
	""" Implement the merge() function below and you should be good to go """
	i = 0	# left
	j = 0	# right
	k = 0	# L

	while i < len(leftL) and j < len(rightL):
		if leftL[i] <= rightL[j]:
			L[k] = leftL[i]
			i += 1
			k += 1
		else:
			L[k] = rightL[j]
			j += 1
			k += 1
	while i < len(leftL):
		L[k] = leftL[i]
		i += 1
		k += 1
	while j < len(rightL):
		L[k] = rightL[j]
		j += 1
		k += 1



def mergeSort(L):
	if len(L) > 1:
		half = len(L) // 2		 # split into two lists
		L1 = L[0:half]
		L2 = L[half:]
		mergeSort(L1)			 # sort each list
		mergeSort(L2)
		merge(L1,L2,L)		     # merge them back into one sorted list


def main():
	N = 10
	L = makeList(N)

	shuffle(L)
	print(L)
	mergeSort(L)
	assert L == makeList(N)
	print(L)


main()

from time import time
from sorts import *

def main():
	N = int(input("N: "))

	L = makeList(N)
	t1 = time()
	selectionSort(L)
	t2 = time()
	print("selection sort time: %8.4f" % (t2-t1))

	t1 = time()
	bubbleSort(L)
	t2 = time()
	print("bubble sort sort time: %8.4f" % (t2-t1))

	t1 = time()
	insertionSort(L)
	t2 = time()
	print("insertion sort time: %8.4f" % (t2-t1))

	t1 = time()
	L.sort()
	t2 = time()
	print("python sort time: %8.4f" % (t2-t1))

main()

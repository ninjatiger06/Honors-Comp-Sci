
#------------------------------------------------------------------------------#
def makeList(N):
    L = []
    for i in range(N):
        L.append(i)
    return L

#------------------------------------------------------------------------------#
def mySort(L):
    """ my sorting algorithm goes here """
    print("in mySort()")
    for i in range(len(L)-1):
        for j in range(len(L)-1):
            val1 = L[j]

            val2 = L[j + 1]

            if val1 > val2 and j < len(L) - 1:
                L[j] = val2
                L[j+1] = val1
                numMoves += 1
        print(L)

    return

#------------------------------------------------------------------------------#
def insertionSort(L):
    """ This is the insertion sort algorithm:
            - assume item at index 0 is already "sorted"
            - starting with item at index 1, check all items to the left and swap positions if needed
            - do the same for item at index 2, where now items at index 0 and 1 should be in order
            - do the same for item at index 3, where now items at index 0, 1, and 2 are in order...and so on

        NOTE: Notice that, for each index, all items to the left are in order, and you are inserting the next item into the correct spot.
    """
    for i in range(1, len(L)-1):
        marker = 2
        for j in range(marker, 0, -1):
            if L[marker]


#------------------------------------------------------------------------------#
def bubbleSort(L):
    """ This is the bubble sort algorithm:
            - given a list L
            - for every item in the list, compare to the item just to the right, swap if needed
            - keep doing the above until you go from one end of the list to the
              other and don't make any swaps!
    """
    for i in range(len(L)-1):       # traverse through all array elements
        # numSwaps = 0

        # last i elements are already in place
        for j in range(0, len(L)-i-1):
            # val1 = L[j]
            # val2 = L[j + 1]
            #
            # if val1 > val2:
            #     L[j] = val2
            #     L[j+1] = val1

            if L[j] > L[j+1]:   # if the first element is bigger than the second, swap
                L[j], L[j+1] = L[j+1], L[j]     # more efficiently swapping the two elements
                # numSwaps += 1

        # if there are no swaps, break early
        # if numSwaps == 0:
        #     break

    return

#------------------------------------------------------------------------------#
def selectionSort(L):
    """ This is the selection sort algorithm:
            - given a list L
            - find the smallest number in the list, swap it to position 0
            - find the next smallest number in the list, swap it to position 1
            - find the next smallest number in the list, swap it to position 2
            - And so on...

        NOTE: It is called selection sort because, each time, you are selecting
        the smallest number from the remaining unsorted elements.
    """
    for i in range(len(L)-1):
        minIdx = i + 1
        for j in range(i, len(L)):
            if L[j] < L[minIdx]:
                minIdx = j

        L[i], L[minIdx] = L[minIdx], L[i]

    return


    #*************************************************************************#
    #          MORE INFO ON THE PYTHON SYNTAX / SHORTHAND SEEN ABOVE          #
    # Swapping 2 items in a list is pretty common in computer programming.
    # In most languages, this is how you do it:
        # tmp = L[ i ]		         # save ith value to temporary location
    	# L[ i ] = L[ j ]	         # copy jth value to ith position
    	# L[ j ] = tmp		         # copy from tmp to jth position

    # This method is perfectly acceptable in Python, but you're welcome to use
    # the shortcut they (Python developers) came up with:
	    # L[j],L[i] = L[i],L[j]
    #*************************************************************************#

#------------------------------------------------------------------------------#
def pythonSort(L):
    """ Use Python's built-in sort() function """
    L.sort()
    return

#------------------------------------------------------------------------------#
def mergeSort(L):
    """
    Here is the basic merge sort algorithm:
        - if the list has two or more items in it, split it into two lists
        - sort each of the two split lists
        - merge the two sorted lists back together into one sorted list

    The merge step is actually not that hard, given two sorted lists.  If you
    know each list is already sorted, you can just compare the first item in each
    list, and take the smaller of the two.A more interesting question is, how
    do we sort each of the split lists? Do we use selection sort, bubble sort,
    or some other sort?

    Since we are talking about merge sort, can we use merge sort to sort each of
    the split lists?  This is called recursion: we are writing a function
    (mergeSort()), and somewhere in that function we call that function
    (or a copy of that function) to help solve the problem.  This may seem odd,
    but it is perfectly fine.  If you think about stack diagrams, calling any
    function just puts another function frame on the stack.  Assuming there is
    an end somewhere, it is perfectly fine for a function to call itself and put
    another copy on the stack.
    """
    pass

#------------------------------------------------------------------------------#
if __name__ == "__main__":
    from random import shuffle

    N = 6
    L = makeList(N)

    # shuffle(L)
    # bubbleSort(L)
    # print(L == makeList(N))
    # assert L == makeList(N)

    # shuffle(L)
    # selectionSort(L)
    # print(L == makeList(N))
    # assert L == makeList(N)

    shuffle(L)
    insertionSort(L)
    assert L == makeList(N)

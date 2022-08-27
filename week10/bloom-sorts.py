"""
    Description: This program contains a variety of sorting algorithms, including:
                        - bubble sort
                        - selection sort
                        - insertion sort
                        - merge sort
    Author: Mr. Bloom
    Date: Fall 2021
"""

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

#------------------------------------------------------------------------------#
def pythonSort(L):
    """ Use Python's built-in sort() function """
    L.sort()
    return

#------------------------------------------------------------------------------#
def bubbleSort(L):
    """ This is the bubble sort algorithm:
            - given a list L
            - for every item in the list, compare to the item just to the right, swap if needed
            - keep doing the above until you go from one end of the list to the
              other and don't make any swaps!
    """
    N = len(L)
    # Traverse through all array elements
    for i in range(N-1):
        # Last i elements are already in place
        for j in range(0, N-i-1):       # Traverse the array from 0 to n-i-1
            if L[j] > L[j+1]:           # Swap if element found is > next element
                L[j], L[j+1] = L[j+1], L[j]
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
    # Traverse through all array elements
    for i in range(len(L)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(L)):
            if L[min_idx] > L[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        L[i], L[min_idx] = L[min_idx], L[i]

    # after the for loop, min_idx should be the index of the smallest item in the list
    # print("smallest is %s" % L[min_idx])
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
    # Traverse through 1 to len(L)
    for i in range(1, len(L)):
        key = L[i]                      # Move elements of L[0..i-1], that are
        j = i-1                         # greater than key, to one position ahead
        while j >= 0 and key < L[j] :   # of their current position
                L[j+1] = L[j]
                j -= 1
        L[j+1] = key

    return

#------------------------------------------------------------------------------#
def merge(leftL, rightL, L):
    """
    To be implemented by you...
    """
    pass

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
    if len(L) > 1:
        half = len(L) // 2		 # split into two lists
        L1 = L[0:half]
        L2 = L[half:]
        mergeSort(L1)			 # sort each list
        mergeSort(L2)
        merge(L1,L2,L)		     # merge them back into one sorted list


#------------------------------------------------------------------------------#
if __name__ == "__main__":
    from random import shuffle

    N = 2000
    L = makeList(N)

    shuffle(L)
    bubbleSort(L)
    assert L == makeList(N)

    shuffle(L)
    selectionSort(L)
    assert L == makeList(N)

    shuffle(L)
    insertionSort(L)
    assert L == makeList(N)

    # add mergeSort() function call after implementing the merge() function



#------------------------------------------------------------------------------#
    #          MORE INFO ON THE PYTHON SYNTAX / SHORTHAND SEEN ABOVE          #
    # Swapping 2 items in a list is pretty common in computer programming.
    # In most languages, this is how you do it:
        # tmp = L[ i ]		         # save ith value to temporary location
    	# L[ i ] = L[ j ]	         # copy jth value to ith position
    	# L[ j ] = tmp		         # copy from tmp to jth position

    # This method is perfectly acceptable in Python, but you're welcome to use
    # the shortcut they (Python developers) came up with:
	    # L[j],L[i] = L[i],L[j]
#------------------------------------------------------------------------------#

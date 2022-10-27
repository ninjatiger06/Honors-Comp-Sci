from math import *

def linearSearch(x, L):
    """ return True if x is in L, False if not """
    for item in L:
        if item == x:
            return True
    # only gets here if not found!
    return False


def binarySearch(x, L):
    """ return True if x is in L, False if not """

    # set a low, middle, and high index
    low = 0
    high = len(L) - 1

    #infinite loop for while the lowest value and highest value are not equal
    while low <= high:
        # index the list at the midpoint and compare that item to the one you're searching for
        mid = (low + high)//2


        listItem = L[int(mid)]
        if listItem == x:
            return True         # if item is found, exit function and return True

        # if item is not found, see if item is lower/higher (less/greater than) the item at the midpoint
        elif x > listItem:
            low = mid + 1

        elif x < listItem:
            high = mid - 1

    return False


def binarySearchIndex(x, L):
    """ return True if x is in L, False if not """

    # set a low, middle, and high index
    low = 0
    high = len(L) - 1

    #infinite loop for while the lowest value and highest value are not equal
    while low <= high:
        # index the list at the midpoint and compare that item to the one you're searching for
        mid = (low + high)//2

        listItem = str(L[int(mid)])
        if listItem == x:
            return mid         # if item is found, exit function and return True

        # if item is not found, see if item is lower/higher (less/greater than) the item at the midpoint
        elif x > listItem:
            low = mid + 1

        elif x < listItem:
            high = mid - 1

    return -1


def binarySearchLOL(x, L):
    """ return True if x is in L, False if not """

    # set a low, middle, and high index
    low = 0
    high = len(L) - 1

    #infinite loop for while the lowest value and highest value are not equal
    while low <= high:
        # index the list at the midpoint and compare that item to the one you're searching for
        mid = int((low + high)/2)

        listItem = L[int(mid)][0]
        if listItem == x:
            return True         # if item is found, exit function and return True

        # if item is not found, see if item is lower/higher (less/greater than) the item at the midpoint
        elif x > listItem:
            low = mid + 1

        elif x < listItem:

            high = mid - 1


if __name__ == "__main__":
    # put test code here
    L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 5
    print("%3d  %s  %s" % (x, str(L), linearSearch(x, L)))
    assert linearSearch(x, L) == True
    x = 500
    print("%3d  %s  %s" % (x, str(L), linearSearch(x, L)))
    assert linearSearch(x, L) == False

    x = 5
    print("%3d  %s  %s" % (x, str(L), binarySearch(x, L)))
    assert linearSearch(x, L) == True
    x = 500
    print("%3d  %s  %s" % (x, str(L), binarySearch(x, L)))
    assert linearSearch(x, L) == False

    x = "c"
    L = "a", "b", "c", "d", "e", "f", "g"
    print("%3s %s %i" % (x, str(L), binarySearchIndex(x, L)))
    assert binarySearchIndex(x, L) == 2

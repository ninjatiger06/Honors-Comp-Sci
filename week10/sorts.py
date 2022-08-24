"""
    Author: Jonas Pfefferman
    Date: 8/23/22
    Description: Different sorting algorithms
"""
from random import shuffle
#-----------------------------------------------------------------------------#
def makeList(N):
    L = []
    for i in range(N):
        L.append(i)
    return L


#-----------------------------------------------------------------------------#
def mySort(L):
    """ my sorting algorithm goes here """
    print("in mySort()")

    MOVE_NEEDED = True

    while MOVE_NEEDED:
        numMoves = 0
        for i in range(len(L)):
            val1 = L[i]

            if i == len(L) - 1:
                val2 = L[0]
            else:
                val2 = L[i + 1]

            if val1 > val2 and i < len(L) - 1:
                L[i] = val2
                L[i+1] = val1
                numMoves += 1

        if numMoves == 0:
            MOVE_NEEDED = False


#-----------------------------------------------------------------------------#
if __name__ == "__main__":

    N = 2000
    L = makeList(N)

    shuffle(L)
    mySort(L)
    assert L == makeList(N)
    print(L == makeList(N))

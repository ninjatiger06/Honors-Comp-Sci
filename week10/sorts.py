"""
    Author: Jonas Pfefferman
    Date: 8/23/22
    Description: Different sorting algorithms
"""

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

    MOVE_PRESENT = True

    print(L)

    while MOVE_PRESENT:
        for i in range(len(L)):
            numMoves = 0
            val1 = L[i]

            if i == len(L) - 1:
                val2 = L[0]
            else:
                val2 = L[i + 1]

            print(val1, val2, val1 > val2)
            if val1 > val2:
                if i == len(L) - 1:
                    L[i] = val2
                    L[0] = val1
                else:
                    L[i] = val2
                    L[i+1] = val1
                numMoves += 1

            if numMoves == 0:
                MOVE_PRESENT = False

            print(numMoves == 0)
            print(L)


#-----------------------------------------------------------------------------#
if __name__ == "__main__":
    from random import shuffle

    N = 2000
    # L = makeList(N)

    # shuffle(L)
    L = [3, 1, 7, 2]
    mySort(L)
    assert L == makeList(N)

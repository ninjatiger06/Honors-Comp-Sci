def maxOfList(L):
    N = len(L)
    if N == 0:                  # If empty do nothing
        return
    if N == 1:                  # Base case
        return L[0]

    leftMax = maxOfList(L[:N/2])         # Find max in left and right portions
    rightMax = maxOfList(L[N/2:])

    if leftMax >= rightMax:            # Return the greater one
        return leftMax
    else:
        return rightMax


def main():
    L = [0, 4, 10, 5, 7]
    print("The largest number is: %d" % maxOfList(L))

main()

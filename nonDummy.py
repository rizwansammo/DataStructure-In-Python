import numpy as np
def printNonDummy(arr, size):
    for i in range(0,size):
        print(arr[i])

arr = np.zeros(6, dtype=int)
arr[0], arr[1], arr[2] = 4, 0, 5
print(arr)
printNonDummy(arr, 3)
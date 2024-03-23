import numpy as np
def reverseOutOfPlace(arr):
    arr2 = np.zeros(len(arr), dtype=int)
    i = 0
    while i < len(arr):
        arr2[i] = arr[len(arr)-1-i]
        i += 1
    print(arr2)

arr = np.array([1, 2, 3, 4])
reverseOutOfPlace(arr)

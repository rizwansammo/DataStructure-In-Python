import numpy as np
def leftShift(arr):
    for i in range(1, len(arr), 1):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = 0
    print(arr) 

arr = np.array([1, 2, 3, 4])
leftShift(arr)
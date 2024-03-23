import numpy as np
def rotateLeft(arr):
    temp = arr[0]
    for i in range(1, len(arr), 1):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    print(arr)

arr = np.array([1, 2, 3, 4])
rotateLeft(arr)
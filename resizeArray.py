import numpy as np
def resizeArray(arr, newSize):
    arr2 = np.array([0]*newSize)
    for i in range(0, len(arr), 1):
        arr2[i] = arr[i]
    return arr2
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
arr2 = resizeArray(arr1, 7)
print(arr2)
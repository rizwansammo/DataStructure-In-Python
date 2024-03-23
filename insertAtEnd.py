import numpy as np

def insertArray(arr, size, elem):
    if size >= len(arr):
        arr = np.resize(arr, len(arr) + 5)
    arr[size] = elem
    return arr

arr = np.zeros(4, dtype=int)
arr[0], arr[1], arr[2] = 4, 6, 5

print(arr)
print(insertArray(arr, 3, 15))  # array, size, elem
print(insertArray(arr, 4, 25))  # array, size, elem

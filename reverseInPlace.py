import numpy as np
def reverseInPlace(arr):
    x, j = 0, len(arr)-1
    for i in range(len(arr)//2):
        arr[x], arr[j] = arr[j], arr[x]
        x += 1
        j -= 1
    print(arr)

arr = np.array([1, 2, 3, 4])
reverseInPlace(arr)

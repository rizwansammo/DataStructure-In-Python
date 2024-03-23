import numpy as np
def rightShift(arr):
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1] 
    arr[0] = 0
    print(arr) 

arr = np.array([1, 2, 3, 4])
rightShift(arr)
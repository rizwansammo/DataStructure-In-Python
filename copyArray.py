import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1 #This is pass by reference
print(arr1)
print(arr2)
#Lets find the memory location of arr1 and arr2
print(id(arr1))
print(id(arr2))
#Prints Same memory location, that means it did not actually copy the array 
#It just created a reference to the same array

#Now lets see how to copy an array with Pass by Value
arr3 = arr1.copy() #This is pass by value
print(arr3)
print(id(arr3))

#We can do it by iteration
def copyArray(arr):
    arr2 = np.array([0]*len(arr))
    for i in range(0, len(arr), 1):
        arr2[i] = arr[i]
    return arr2

arr4 = copyArray(arr1)
print(id(arr1))
print(id(arr4))
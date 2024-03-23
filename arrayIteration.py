import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print('Using Regular For Loop')
for i in arr1:
    print(i)

print('Using ranged For Loop')
for i in range(0,len(arr1),1):
    print(arr1[i])
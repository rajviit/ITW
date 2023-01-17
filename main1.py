import array as a
import numpy as np

arr = a.array('i',[])
result = a.array('i',[])
n = int(input("Enter the Size of array : "))
for i in range(0,n):
    p = int(input("Enter the Element: ", ))
    arr.append(p)

print("The array is :", arr)

rev = arr[::-1]
print("The reverse array is :", rev)

print("The addition of two arrays is : ", np.add(arr,rev))

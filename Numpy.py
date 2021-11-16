import numpy as np
"""
Numpy is an array-processing package. 
It is a multidimensional array object, and tools for working with arrays. 
It is a very important package for scientific computing with Python.
Other than the scientific uses, Numpy can also be used as an effective multi-dimensional container of data.
"""
# Array 1
r1 = np.array([[10, 4], [8, 13]], 
                 dtype = np.float64)
                  
# Array 2
r2 = np.array([[19, 7], [11, 5]], 
                 dtype = np.float64) 
 
# Adding of two Arrays
total = np.add(r1, r2)
print("Addition of Two Arrays: ")
print(total)
 
# Adding of all Array elements
Sum_all = np.sum(r1)
print("\nAddition of Array elements: ")
print(Sum_all)
 
# Square root of Array
Sqrt = np.sqrt(r1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)
 
# Transpose of Array
# using In-built function 'T'
Trans = r1.T
print("\nTranspose of Array: ")
print(Trans)
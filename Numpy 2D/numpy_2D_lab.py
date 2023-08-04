import numpy as np

#Creating a 2D list

a = [[11,12,13], [21,22,23], [31,32,33]]
print(a)

#Converting list to Numpy Array
#Every element is the same type

A = np.array(a)
print(A)

#Showing numpy array dimensions, shape, size

print(A.ndim)
print(A.shape)
print(A.size)

#Accessing different elements of the numpy array

print(A[1,2])
print(A[1][2])

#Accessing the first row first column

print(A[0][0])

# Access the element on the first row and first and second columns

print(A[0][0:2])

# Access the element on the first and second rows and third column

print(A[0:2, 2])
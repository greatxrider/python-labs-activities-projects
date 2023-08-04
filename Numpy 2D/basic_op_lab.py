import numpy as np
import matplotlib.pyplot as plt

#Basic Operations

x = np.array([[1, 2], [0,1]])
print(x)

y = np.array([[2,1], [1,2]])
print(y)

#Addition
Z = x + y
print("Addition: ",Z)

#Multiplication with scalar
C = y * 2
print("Multiplication: ",C)

#element wise multiplication
D = x * y
print("Element wise multiplication: ", D)

#Matrix Multiplication
A = np.array([[0,1,1], [1,0,1]])
B = np.array([[1,1], [1,1], [-1,1]])

e = np.dot(A,B)
print("Matrix multiplication: ", e)

#calcuating the sine of Z
X = np.sin(e)
print("Sine function: ", X)

#transposed matrix
C = B.transpose()
D = B.T
print("Transposed matrix: ", C)
print("Transposed matrix: ", D)
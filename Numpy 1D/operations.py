import numpy as np
import matplotlib.pyplot as plt

#numpy operations

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr_add = np.add(arr1, arr2)
print(arr_add)

#array subtraction
a = np.array([10, 20, 30])
b = np.array([5, 10, 15])
c = np.subtract(a, b)
print(c)

#array multiplication
 
x = np.array([1,2])
y = np.array([2,1])
z = np.multiply(x,y)
print(z)

#array division

d = np.array([10, 20, 30])
e = np.array([2, 10, 5])
f = np.divide(d, e)
print(f)

#dot_product
g = np.array([1,2,3])
h = np.array([2,1,3])
i = np.dot(g,h)
print(i)

#Adding constant to a Numpy Array
j = np.array([1,2,3,-1])
print(j+1)

#Mathematical Functions
#pi
k = np.pi
l = np.array([0, k/2, k])
print(l)

#sin
m = np.sin(k)
print(m)

#Linspace
#numpy.linspace(start, stop, num = int value)

n = np.linspace(-2,2,num=9)
print(n)

# Make a numpy array within [0, 2π] and 100 elements 

o = np.linspace(0, 2*np.pi, num=100)
print(o)

# Calculate the sine of o list

p = np.sin(o)
print(p)

# Plot the result

plt.plot(o, p)
#plt.show()

#Iterating 1-D Arrays
#forloops
arr3 = np.array([1, 2, 3, 4, 5])
for x in arr3:
    print(x)
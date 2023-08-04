# quiz on numpy array 1 Dimensional
import numpy as np
import time
import sys
import matplotlib.pyplot as plt

# Implement the following vector subtraction in numpy: u-v
u = np.array([1,0])
v = np.array([0,1])
z = np.subtract(u,v)
print(z)

# Multiply the numpy array z with -2:
a = np.array([2,4])
x = a*(-2)
print(x)

# Consider the list [1,2,3,4,5] and [1,0,1,0,1], 
# and cast both lists to a numpy array then multiply them together:

list_1 = np.array([1,2,3,4,5])
list_2 = np.array([1,0,1,0,1])
mult_list = np.multiply(list_1,list_2)
print(mult_list)

#Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. 
#Then, plot the arrays as vectors using the fuction Plotvec2 
#and find their dot product:

c = np.array([-1,1])
d = np.array([1,1])


def Plotvec2(c,d):
    ax = plt.axes()
    ax.arrow(0,0,*c, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(c+0.1),'c')
    ax.arrow(0,0,*d, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(d+0.1),'d')
    
    plt.ylim(-2,2)
    plt.xlim(-2,2)

Plotvec2(c,d)
plt.show()

e = np.dot(c,d)
print(e)

#Convert the list [1, 0] and [0, 1] to numpy arrays a and b. 
# Then, plot the arrays as vectors using the function Plotvec2 and 
# find their dot product:

c = np.array([1,0])
d = np.array([0,1])

Plotvec2(c,d)
plt.show()
e = np.dot(c,d)


#Convert the list [1, 1] and [0, 1] to numpy arrays a and b. 
# Then plot the arrays as vectors using the fuction Plotvec2 and 
# find their dot product:

c = np.array([1,1])
d = np.array([0,1])

Plotvec2(c,d)
plt.show()
e = np.dot(c,d)

#Why are the results of the dot product for [-1, 1] and [1, 1] 
# and the dot product for [1, 0] and [0, 1] zero, but not zero 
# for the dot product for [1, 1] and [0, 1]?

#Because the two arrays are perpendicular, and the non-zero arrays 
#are not.

#Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2. 
#Then perform Addition , Subtraction , Multiplication , Division and 
#Dot Operation on the arr1 and arr2.
arr1 = np.array([1,2,3])
arr2 = np.array([8,9,10])

#Addition 
arr_add = np.add(arr1,arr2)
#Subtraction
arr_subtract = np.subtract(arr1,arr2)
#Multiplication
arr_multiply = np.multiply(arr1,arr2)
#Division
arr_divide = np.divide(arr1,arr2)
#Dot Operation
arr_dot = np.dot(arr1,arr2)

print(arr_add)
print(arr_subtract)
print(arr_multiply)
print(arr_divide)
print(arr_dot)

#Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy 
# arrays arr1 and arr2. Then find the even and odd numbers 
# from arr1 and arr2.

list_1 = np.array([1,2,3,4,5])
list_2 = np.array([6,7,8,9,10])
#even numbers
even_list1 = list_1[1:5:2]
even_list2 = list_2[0:5:2]
print(even_list1)
print(even_list2)
#odd numbers
odd_list1 = list_1[0:5:2]
odd_list2 = list_2[1:5:2]
print(odd_list1)
print(odd_list2)

#SCORE 100/100
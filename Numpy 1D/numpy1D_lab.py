#importing numpy as np
import numpy as np

#Creating a Python List and accesing using index
a = ["0", 1, "two", "3", 4]
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#creating a numpy array
b = np.array([0, 1, 2, 3, 4])
#printing each element
print("b[0]:", b[0])
print("b[1]:", b[1])
print("b[2]:", b[2])
print("b[3]:", b[3])
print("b[4]:", b[4])

#checking num_py version
print(np.__version__)
print(np.version.version)

#Type of array
type(a)
type(b)

#Check type of value inside array
print(b.dtype) 

#checking type of the array and value type
c = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(c.dtype)

#Assigning value on certain index
c[0] = 200
c[1] = 20
print(c)

#Slicing
d = c[1:4]
print(d)

#Assigning value to two indexes at once
c[3:5] = 300, 400
print(c)

#define the steps in slicing, like this: [start:end:step]
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])

#print an end only
print(arr[:4])

#print a start only
print(arr[4:])

#printing without the step
print(arr[1:5:])

#printing only the even elements of the array
array_2 = np.array([1,2,3,4,5,6,7,8,9,10])
print(array_2[1:10:2])

#Assigning value with list
select = [0, 2, 3, 4 ]

#using list to select elements
d = c[select]
print("this is d: ", d)

# Assign the specified elements to new value

#c[select] = 100000
#print(c)
#[1.e+05 2.e+01 1.e+05 1.e+05 1.e+05]

#Other Attributes
# Create a numpy array
f = np.array([0, 1, 2, 3, 4])
print(f)

# Get the size of numpy array
print(f.size)

# Get the number of dimensions of numpy array
print(f.ndim)

# Get the shape/size of numpy array
print(f.shape)

#Statistical functions
g = np.array([1, -1, 1, -1])

# Get the mean of numpy array

mean = g.mean()
print(mean)

# Get the standard deviation of numpy array

standard_deviation=g.std()
print(standard_deviation)

# Create a numpy array

h = np.array([-1, 2, 3, 4, 5])
print(h)

# Get the biggest value in the numpy array

max_h = h.max()
print(max_h)

# Get the smallest value in the numpy array

min_h = h.min()
print(min_h)

#Numpy Array Operations
#Array Addition

u = np.array([1, 0])
v = np.array([0, 1])

z = np.add(u, v)
print(z)

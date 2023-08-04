import numpy as np
import time
import sys
import matplotlib.pyplot as plt

#Array Addition
u = np.array([0,1])
v = np.array([1,0])
z = np.add(u,v)

#plotting functions

def Plotvec1(u,z,v):
    #generate full window axes
    ax = plt.axes()
    # Add an arrow to the U Axes with arrow head width 0.05, 
    # color red and arrow head length 0.1
    ax.arrow(0,0,*u, head_width=0.05, color='r', head_length=0.1)
    #Addts the text u to the Axes
    plt.text(*(u+0.1),'u')
    
    # Add an arrow to the v Axes with arrow head width 0.05, 
    # color red and arrow head length 0.1
    ax.arrow(0,0,*v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v+0.1),'v')
    
    #Add arrow for z
    ax.arrow(0,0,*z, head_width=0.05, color='g', head_length=0.1)
    #adds the text z to the Axes
    plt.text(*(z+0.1),'z') 
    
    #set the ylim to bottom(-2), top(2)
    plt.ylim(-2,2)
    #set the ylim to left(-2), right(2)
    plt.xlim(-2,2)
    
Plotvec1(u,z,v)
plt.show()
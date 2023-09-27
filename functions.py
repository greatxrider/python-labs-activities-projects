#
# FUNCTIONS
#

# Generally, the syntax for a function is:
def any_function_name(any_parameters):
    # Codes
    #return any_output
    print("Codes related to function ...")




# As an example, we create functions for
# addition and substraction


# Calling a Function
def my_function():
    print("Hello from a function")

my_function() # This is how you call the function


# Parameters
def my_function2(fname):
    print(fname + " Refsnes")

my_function2("Emil") # Emil Refsnes
my_function2("Tobias") # Tobias Refsnes
my_function2("Linus") # Linus Refsnes


# Now try to swap parameters in the "addition" function

# Also, try to have less than 2 parameters
# Also, try to have more than 2 parameters


# Default Parameter Value
def my_function3(country = "Norway"):
    print("I am from " + country)

my_function3("Sweden")
my_function3("India")
my_function3()
my_function3("Brazil")



#
# RECURSION
#



# Generally, the syntax for Recursion is
def any_function_name2(any_parameters):
    if any_parameters==0: # apply terminating condition
        print("Loop terminates at this BASE CONDITION")
    else:
        print("Call its self again")

# Why do you think it is necessary to have BASE CONDITION?


# Example 1
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results")
tri_recursion(6)


# Example 2
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)


#
# CHALLENGES
#

# Challenge 1
# Create a function that do the Countdown
# Hint: Use for/while loop


# Challenge 2
# Create a RECURSIVE function that do the Countdown



#
# ANSWERS TO CHALLENGES
#
#
# Challenge 1
# Create a function that do the Countdown
# Hint: Use for/while loop
def countdown1(n):
    for i in range(n,-1, -1):
        print(i)
countdown1(5)

# Challenge 2
# Create a RECURSIVE function that do the Countdown
def countdown2(n):
    if n==0:
        print(n)
    else:
        print(n)
        return countdown2(n-1)

countdown2(5)
#1 Provide a Python implementation of a function first_N that takes a positive integer, n, as its only argument. The function should print the first n perfect squares that are not even numbers. Example, if n is 2, it should print the perfect squares 1 and 9. 
def first_N(n):
    if n<4:
        for x in range(n+3):
            if x%2!=0:
                z=x**2
                print(z)
    if n==4:
        for x in range(n+5):
            if x%2!=0:
                s=x**2
                print(s)
    else:
        for x in range(n+6):
            if x%2!=0:
                s=x**2
                print(s)
#2 





#3 Write a function that computes the list of the first 30 Fibonacci numbers.
def Fib(y):
    if y==0 or y==1:
        return y
    else:
        return Fib(y-1) + Fib(y-2)

#4 Write a function that combines two lists by alternatingly taking elements. For example, given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3] 
def combine(n1,n2,n3):
    xs = ["a",n1,"b",n2,"c",n3]
    print(xs)


#5Write a function that given a list of non-negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021. 
def mynumbers(a,c,e,g):
    return g+e+c+a


#6 Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion. 

i = [0,1,2,3,4,5,6,7,8,9,10]
z = sum(i)
print(z)

#7
i = [0,1,2,3,4,5,6,7,8,9,10]
for x in i:
    while x<0:
        print(x)
        x+=1


    
if __name__ == "__main__":
    a=input("\nEnter number for number 1")
    b = int(a)
    print(first_N(b))

    y=int(input("\nEnter number for number 3"))
    print(Fib(y))

    b=input("\nEnter a number, #for number 3\n")
    a=str(b)
    d=input("\nEnter a number greater than your previous number\n")
    c=str(d)
    f=input("\nEnter a number greater than your previous number\n")
    e=str(f)
    h=input("\nEnter a number greater than all your previous number\n")
    g=str(h)
    print("Largest number formed by all your numbers")
    print(g+e+c+a)

    n1=input("\ntype number for number 4\n")
    n2=input("\ntype number greater than your previous\n")
    n3=input("\ntype number greater than all your number\n")
    print(combine(n1,n2,n3))
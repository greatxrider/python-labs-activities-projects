
def first_N(n):
    x = 0
    while x<n*2:
        x+=2
        if x%2==0:
            z = x**2
        print(z)
        
    

def smallest_number(numbers):
    xs = ""
    for x in numbers:
        xs+=x
    print(" ")    
    print('Smallest possible number of non-negative integers:',xs)
    


def productforloop(Poop):
    xs = 1
    for x in Poop:
        xs=xs*x
    print(" ")
    print ('Product of numbers in number list using For Loop:', xs)
    print(" ")




def productwhileLoop(n):
    product = 1
    x = 1
    while x <= n:
        product=product*x
        x+=1
    print("")
    print ('Product of numbers using While Loop:', product)    



def productrecursive(items):
    if len(items) == 1:
        return items[0]
    return items[0] * productrecursive(items[1:])

#6 sa mga values daw sa list, range sugod sa 1 dayon Kuhaon dayon ang maximum sa list or (max(n)) addan dayon og 1, kung ang a daw kay equal daw siya sa 1
#iappend daw niya ang 1 sa ys kundili equal iappend niya kay zero. pagkahuman i append niya ang ys sa xs thus ang tanan values sa ys kay mapadung sa xs.

def transform(n):
    xs = []
    for i in n:
        ys = []
        for a in range(1,max(n)+1):
            if a==1:
                ys.append(1)
            else:
                ys.append(0)
        xs.append(ys)
    return xs

if __name__ == "__main__":
    
    print("How many perfect n squares")
    a=input()
    b=int(a)
    first_N(b)
    
    print("Enter number for number 2")
    a = input()
    b = input("\nEnter 2nd number\n")
    c = input("\nEnter 3rd number\n")
    d= input("\nEnter 4th number\n")
    z =[a,b,c,d]
    y = sorted(z)
    smallest_number(y)

    Numbers = [1,2,3,4,5,6,7,8,9,10]
    productforloop(Numbers)

    print("Enter value of n for While x<n (10 brings 3628800)")
    Whileloop = int(input())
    productwhileLoop(Whileloop)

    items = [1,2,3,4,5,6,7,8,9,10]
    print ("Product of list using Recursive",productrecursive(items))
    

    print("")
    print('Two-dimensional list:',transform([1,2,3,4,5,2,3,1]))






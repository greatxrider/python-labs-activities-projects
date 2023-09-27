# Import the functions from module1.py

def sort_two_numbers(x,y):
    pass

def sort_list(xs):
    pass




if __name__ == "__main__":
    # Challenge 1: sort numbers n1 and n2 using get_max or get_min
    # Expected result where k1<k2 ->  [k1,k2] 
    n1 = int(input("Number 1:  "))  
    n2 = int(input("Number 2:  "))  
    print(sort_two_numbers(n1,n2))

    # Challenge 2: sort the list in ascending order 
    # using get_max or get_min
    # Expected result from xs=[3,2,1] is ys=[1,2,3]
    xs = []
    size = 3
    for i in range(size):
        xs.append(int(input("Number {}: ".format(i+1))))
    print(sort_list(xs))
#1.Given the code snipet below, concatenate to print the sentence, "I am Lee. I like going to school."
name = 'Lee.'
a = "I am"
b = "I like going to "
mall = "school."
print(a + " " + name + " " + b + ""+ mall)

#2.Current is a measure of the flow electric charge Q over time.......
# Given t = 1 (Amp)
i = 1
print("Time in Seconds")
time = input()
FlowofElectricChargeQ = i*time
print(FlowofElectricChargeQ)

#6. Create a generic program that compare two ages.....
print("How old are you?")
You = input()
YourBestFriend = input("\nHow old is your Best friend\n")
if You > YourBestFriend:
    print("You are older than Your Best Friend")
elif You == YourBestFriend:
        print("You are the same of Age")
else:
    print("Your Best Friend is older than you")

#4 The string "A quick  brown fox jumps over the lazy....
string = ("A quick brown fox jumps over the lazy dog")
How = string.split()
print(len(How))
100, 99, 87, 78, 65, 43, 24, 23, 12, 8, 3, 1, 0
#7 Sort the list [23, 24, 12, 8, 3, 43, 78, 65, 87, 99, 100, 1, 0]
numberlist = [23, 24, 12, 8, 3, 43, 78, 65, 87, 99, 100, 1, 0]
numberlist.remove(23)
numberlist.remove(24)
numberlist.remove(12)
numberlist.remove(8)
numberlist.remove(3)
numberlist.remove(43)
numberlist.remove(78)
numberlist.remove(65)
numberlist.remove(87)
numberlist.remove(99)
numberlist.remove(100)
numberlist.remove(1)
numberlist.remove(0)
numberlist.append(100)
numberlist.append(99)
numberlist.append(87)
numberlist.append(78)
numberlist.append(65)
numberlist.append(43)
numberlist.append(24)
numberlist.append(23)
numberlist.append(12)
numberlist.append(8)
numberlist.append(3)
numberlist.append(1)
numberlist.append(0)
print(numberlist)

#3. Create a program that solves the hyperbolic tangent....

anyrealnumber_X = input(float())
e =  2.718
b = ((e**anyrealnumber_X)-(e**-anyrealnumber_X))/((e**anyrealnumber_X)+(e**-anyrealnumber_X))
print(b)

#15 Display all integer that is divisibleby 15...
x = 0
while x < 1001:
    print(x)
    x+=15

#5 Transform the string "hello, world!"....
string_2 = "hello, world!"
f = string_2.replace("w", "W")
g = f.replace("h", "H")
print(g)

#11 Given a sorted list [2, 4, 6, 8, 10].....
givenlist = [2, 4, 6, 8, 10]
n = input(int())
if n%2==0:
    givenlist.append(n)
elif n < givenlist:
    givenlist.append(n)
print(givenlist)

   



















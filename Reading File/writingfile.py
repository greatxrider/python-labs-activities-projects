exmp2 = './Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open(exmp2, 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
with open(exmp2, 'a') as writefile:
    writefile.write("This is line D\n")
    writefile.write("This is line E\n")
    writefile.write("This is line F\n")
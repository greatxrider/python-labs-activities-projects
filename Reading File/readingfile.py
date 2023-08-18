example1 = "example1.txt"
file1 = open(example1, "r")
print("File path:", file1.name)
print("File path:", file1.mode)

FileContent = file1.read()
print(FileContent)
print(type(FileContent))
file1.close()

#Other Alternative

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
    
print(file1.closed)

with open(example1, "r") as file1:
    FileContent=file1.read(4)
    print(FileContent)

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(40))
 
with open(example1, "r") as file1:
    FileasList = file1.readlines()
    FileasList[0]
    FileasList[1]

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
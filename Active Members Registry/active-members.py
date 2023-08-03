#Jeph Mari Daligdig - August 2023
#Program Separates active and inactive members from a file and writes them to separate files.

def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            writeFile.seek(0)
            members = writeFile.readlines()
            header = members[0]
            members.pop(0)
            inactive = [member for member in members if ('no' in member)]
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()      
            
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)
headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read()) 
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
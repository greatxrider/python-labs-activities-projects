# a+
# Copy file to another

ex2 = "./Example2.txt"
ex3 = "./Example3.txt"
with open(ex2, "r") as readfile:
    with open(ex3, "w") as writefile:
        for line in readfile:
            writefile.write(line)
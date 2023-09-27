#Jeph Mari Daligdig - Faces
#Problem set 0

def convert(userInput):
    happySadInput = userInput.replace(":)","🙂").replace(":(","🙁")
    return happySadInput

userInput = input("Please Enter a smiley: ")
print(convert(userInput))
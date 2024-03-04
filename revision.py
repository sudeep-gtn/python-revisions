name = ""
while(name == ""):
    name = str(input("Enter your name : "))
    if(name):
        continue
    else :
        print("Please enter your name: ")
print("Hello " + name)
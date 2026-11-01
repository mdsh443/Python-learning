# Nesting in conditional statements: 
age = int(input("Enter your age: "))
if (age >= 18):
    if (age > 80):
        print("You are not allowed to drive, since you are over 80")
    else:
        print("You can drive")
else:
    print(f"You are not allowed to drive, since you are {age}")
#Q.1: Write a program to check if a number is odd or even number:
number = int(input("Enter number: "))
if (number % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")
    
# num = int(input("Enter number: "))
# reminder = num % 2
# if (reminder == 0):
#     print("The number is even")
# else:
#     print("The number is odd")

# Q.2: Write a program to find the largest of three numbers entered by the user:
n = int(input("Enter 1st number: "))
m = int(input("Enter 2nd number: "))
p = int(input("Enter 3rd number: "))
if (n>=m and n>=p):
    print(f"1st is the largest number, {n}")
elif (m>=p):
    print(f"2nd is the largest number, {m}")
else:
    print(f"3rd is the largest number, {p}")
    
#Q.2.1: Write a program to find the largest of four numbers entered by the user:
n = int(input("Enter 1st number: "))
m = int(input("Enter 2nd number: "))
p = int(input("Enter 3rd number: "))
q = int(input("Enter 4th number: "))

if (n>=m and n>=p and n>=q):
    print(f"1st is the largest number, {n}")
elif (m>=p and m>=q):
    print(f"2nd is the largest number, {m}")
elif (p>=q):
    print(f"3rd is the largest number, {p}")
else:
    print(f"4th is the largest number, {q}")
    
#Q.2.2: Write a program to find the largest of four numbers entered by the user and 
# what if multiple numbers entered by user are equal:
n = int(input("Enter 1st number: "))
m = int(input("Enter 2nd number: "))
p = int(input("Enter 3rd number: "))
q = int(input("Enter 4th number: "))

if (n>=m and n>=p and n>=q):
    print(f"1st is the largest number, {n}")
if (m>=n and m>=p and m>=q):
    print(f"2nd is the largest number, {m}")
if (p>=n and p>=m and p>=q):
    print(f"3rd is the largest number, {p}")
if (q>=n and q>=m and q>=p):
    print(f"4th is the largest number, {q}")
    
#Q.3: Write a program to find out if a number is a multiple of 3 or not:
nu = int(input("Enter number: "))
if (nu % 3 == 0):
    print(f"The number is a multiple of 3 and the number: {nu}")
else:
    print(f"The number is not a multiple of 3 and the number: {nu}")
    

    
    


#Q.1: Write a program to input 2 numbers and print their sum: 
num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))
sum = num_1 + num_2
print(f"Sum of two numbers: {sum}")
# print(f"Sum of two numbers: {(num_1 + num_2)}")

#Q.2: Write a program to input side of a square and print its area:
side = float(input("Side of a square: "))
area = (side * side)  # area = (side ** 2) => ei bhabeo solve kora jeto.
print(f"Area of a square: {area}")

#Q.3: Write a program to input 2 floating point numbers & print their average:
number1 = float(input("Enter number1: ")) 
number2 = float(input("Enter number2: ")) 
average = (number1 + number2)/2
print(f"Average of two numbers: {average}")

#Q.4: Write a program to input 2 integer numbers, a and b.
#     print True if a is greater than or equal to b. If not print False.
a = int(input("num1: "))
b = int(input("num2: "))
c = (a>=b)
print(c)
# print(f"Answer: {(a>=b) and (a>=b)}")

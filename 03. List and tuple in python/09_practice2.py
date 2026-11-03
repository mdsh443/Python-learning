#Q.2: write a program to check if a list contains a palindrome of contents.
num = [1,2,2,1]
reversed_num = num.copy()
reversed_num.reverse() 
print(reversed_num)
if reversed_num == num:
    print("Palindrome")
else:
    print("Not palindrome")
    
  #############################  
name = ["m", "a", "a", "m",]
copy_name = name.copy()
copy_name.reverse()
if copy_name == name:
    print("palindrome")
else:
    print("not palindrome")
##############################

#Q.3: write a program to count the number of students with the "A" grade
#     in the following tuple: 
grade = ("C", "D", "A", "A", "B", "B", "A",)
print(grade.count("A"))

#Q.4: write a program to store the above values in a list & 
#     sort the from "A" to "D".
grade_list = ["C", "D", "A", "A", "B", "B", "A",]
grade_list.sort()
print(grade_list)
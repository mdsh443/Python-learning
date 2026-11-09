#Q.1: Store following word meanings in a python dictionary:
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

meanings = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal",
}
print(meanings)

#Q.2: You are given a list of subjects for students. Assume one classroom is required 
# for one subject. How many classrooms are needed by all students?
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"

subjects = {"python", "java", "C++", "python", 
            "javascript", "java", "python", "java", "C++", "C"}

print(subjects)
print(len(subjects))

#Q.3: write a program to enter marks of 3 subjects from the user and store them in a 
# dictionary.start with an empty dictionary and add one by one. Use subjects name 
# as key and marks as value.

marks = {}
x = int(input("Enter PHY marks: "))
marks.update({"PHY" : x})

y = int(input("Enter CHEM marks: "))
marks.update({"CHEM" : y})

z = int(input("Enter MATH marks: "))
marks.update({"MATH" : z})

print(marks)

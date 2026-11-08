#nested dictionary:
print("\nStart of this program\n")

student = {
    "name" : "nawaz",
    "subjects" : {                 # nested dictionary
        "PHY" : 89,
        "CHY" : 88,
        "MATH" : 55,
    },
    "age" : 33,
    "likes" : "Python"
}

print(student)
print(student["age"])
print(student["subjects"])
print(student["subjects"]["PHY"])
print(student["subjects"]["MATH"])

print("\nEnd of this program\n")

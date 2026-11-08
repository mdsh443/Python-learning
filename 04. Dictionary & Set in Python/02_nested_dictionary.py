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

#Q.1: change the student’s "MATH" mark from 55 to 75, then print the updated mark.
student["subjects"]["MATH"] = 75
student["subjects"]["ENG"] = 90
print(student["subjects"])
print(student["subjects"]["ENG"])

# Q.2: Write two lines to:
# 1. Change "eth1" from "down" to "up".
""" device = {
    "name": "Router1",
    "interfaces": {
        "eth0": "up",
        "eth1": "down"
    }
} """
# 2. Print only the updated status of "eth1".

device = {
    "name": "Router1",
    "interfaces": {
        "eth0": "up",
        "eth1": "down"
    }
}
device["interfaces"]["eth1"] = "up"
print(device["interfaces"]["eth1"])

print("\nEnd of this program\n")
# .keys()
# .values()
# .items()
# .get()
# .update()

# method 1: .keys():================
print("\nStart of this program\n")

student = {
    "name" : "nawaz",
    "subjects" : {                 
        "PHY" : 89,
        "CHY" : 88,
        "MATH" : 55,
    },
    "age" : 33,
    "like" : "Python"
}
print(student.keys())              #nested keys will not be printed
print(list(student.keys()))        # type casted output=> dictionary to list
print(len(list(student.keys())))   # output list length

print("\nEnd of this program\n")

# method 2: .values():=================
print(student.values()) 
print(list(student.values()))       # amra dictionary er moddhe list store korte pari
print(len(list(student.values())))  # abar list er moddheo dictionary store korte pari 

print("\nEnd of this program\n")

# method 3: .items():
#print(student.items())    # dictionary er key, value ke ekta tuple hishebe print kore
print(list(student.items()))    # now output ta ekta list list a converted       
pairs = list((student.items())) 
print(pairs[0])    
print(pairs[1])            # output list er index print korce
print(pairs[2])     

print("\nEnd of this program\n")

# method 3: .get():
print(student["name"])
print(student.get("name"))

print("\nEnd of this program\n")

fish = {
    "rohu" : {
        "price" : 45,
        "test" : "good",
    },
    "ilish" : {
        "price" : 200,
        "test" : "very good",
    },
    "buy" : "all"
}

print(fish)
# method 4: .get():================
#new_dict = {"cook" : "ilish"}
#fish.update(new_dict)
fish.update({"cook" : "ilish", "dinner": "tonight", "time" : 8.00})
print(fish)

print("\nEnd of this program\n")

           
                      
                  
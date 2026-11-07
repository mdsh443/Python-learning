# dictionary comes as a key : value pair. "Keys" can not be list or dictionary. 
# "keys" can be numbers, string, float, boolean, etc. "values" can be all type. 
# majority scenario te keys and values strings e hoi. 
# Python dictionaries are unordered. Means there is no index number like 
# list or tuples. Like list, dictionary is also mutable. 
# We can't create duplicate keys.
print("\nStart of the program\n")

info = {
    "name" : "newaz",             # "name"=>(key) : "newaz"=>(value) => string
    "cgpa" : 9.6,                 # "cgpa"=>(key) : 9.6=>(value) => float
    "marks" : [98, 97, 95],       # "marks"=>(key) : [98, 97, 95]=>(value) => list
    "age" : 33,                   # "age"=>(key) : 33=>(value) => integer
    "is_adult" : True,            # "is_adult"=>(key) : True=>(value) => Boolean 
    "subjects" : ["python", "C++", "java"],
    "topics" : ("dictionary", "set"),#"topic"=>(key) : ("dictionary, "set")=>(value) => tuples
}
info["name"] = "Marshia"
info["is_adult"] = False

print(info)
print(type(info))
print(info["name"])
print(info["is_adult"])
print(info["age"])
print(info["subjects"])
# print(info["surname"])

print("\nEnd of the program\n")

null_dict = {}                # We started with a empty dictionary
null_dict["name"] = "Newaz"   # Then we put value inside the dictionary
print(null_dict)

print("\nEnd of the program\n")


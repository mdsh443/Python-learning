# set.add(el)
# set.remove(el)
# set.clear()
# set.pop()
# set is mutable but the elements of set are immutable. 

#method.1: set.add()==============
print("\nStart of the program\n")

collection = set()
collection.add(1)
collection.add("rinthy")
collection.add("90.111")
collection.add(False)
collection.add("newaz")

collection.remove("newaz")
collection.remove(1)

print(collection)
print(type(collection))

print("\nEnd of the program\n")

# method.2: set.remove()
num = {200, 2, 3, "newaz", "rinthy", "muadib", False, 12.111}
num.add("joshim")
num.add((99, 23, 55, "baba_yaga")) # tuple can be set element bcz it is immutable
# num.add({20, 1222, 34}) # list can not a set element bcz it is mutable
num.remove(200)
num.remove("rinthy")
#num.remove(10.111) #this will give an error because 10.111 is not an element of this set
print(num)
print(len(num))
print(type(num))

print("\nEnd of the program\n")

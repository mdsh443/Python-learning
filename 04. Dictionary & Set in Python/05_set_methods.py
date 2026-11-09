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
collection.add(90.111)
collection.add(False)
collection.add("newaz")

collection.remove("newaz")
collection.remove(1)

print(collection)
print(type(collection))

print("\nEnd of the program\n")

# method.2: set.remove() ====================
num = {200, 2, 3, "newaz", "rinthy", "muadib", False, 12.111}
num.add("joshim")
num.add((99, 23, 55, "baba_yaga")) # tuple can be set element bcz it is immutable
# num.add({20, 1222, 34}) # list can not a list element bcz it is mutable
num.remove(200)
num.remove("rinthy")
#num.remove(10.111) #this will give an error because 10.111 is not an element of this set
print(num)
print(len(num))
print(type(num))

print("\nEnd of the program\n")

#method.3: set.clear(): ===========================
r_set = {200, 2, 3, "usul", "lisan_al_gaib", "muadib", True, 12.111}
print(r_set.clear())     #clears the whole set .clear()

print("\nEnd of the program\n")

#method.4: set.pop(): ==========================
num_5 = {200, 2, 3, "usul", "lisan_al_gaib", "muadib", True, 12.111}
print(num_5.pop())
print(num_5.pop())      # Removes and returns an arbitrary element
print(num_5.pop())

################################

devices = {"Router", "Switch", "Firewall"}
removed_device = devices.pop()

print(f"Removed: {removed_device}")
print(f"Remaining: {devices}")

print("\nEnd of the program\n")


#method.5: set.union(): =====================
set_8 = {1, 2, 3}
set_9 = {2, 3, 4, 5}

print(set_8.union(set_9))
print(set_8.intersection(set_9))

print("\nEnd of the program\n")

#method.6: set.intersection(): =====================

network_a = {"Router", "Switch", "Firewall"}
network_b = {"Switch", "Firewall", "Server"}

all_devices = network_a.union(network_b)
common_devices = network_a.intersection(network_b)

print(all_devices)
print(f"Total unique device types: {len(all_devices)}")
print(common_devices)
print(f"Common device types: {len(common_devices)}")

print("\nEnd of the program\n")



# list.remove(): removes the first occurrence of an element from a list.
list = [2, 1, 4, 23, 90, 90, 22, 11]
list.append(100)
# list.sort()
list.insert(3, 222)
list.remove(90)  #removes the first 90 from the list and keeps the 2nd 90.
print(list)

#P.2:
name = ["alice", "nawaz", "joshim", "rinthy", "adam"]
name.append("ana")
name.remove("joshim")
print(name)

#.pop(): list er moddhe specific element ke remove kore:
name1 = ["alice", "nawaz", "joshim", "rinthy", "adam"]
# name1.append("josim")
# name1.remove("joshim")
name1.pop(3)
print(name1)

# remove() deletes by value. pop() deletes by position and returns the deleted item.

# .reverse() => list ke just reverse kore dei but kono order maintain kore na.
# P.1:
list = ["a", "b", "c", "e", "d", "m", "p"]
list.append("z")
list.reverse()
print(list)

#P.2: 
fruit = ["apple", "mango", "banana", "blue_berry", "cherry"]  # fruit list
fruit.append("lichi")                          # append "lichi"
fruit.sort()                                   # sort.() the appended list orderly
print(fruit.reverse(), fruit)                  # just reverse the list

#P.3: 
num = [12, 34, 11, 123, 90, 31]    # number list
num.append(100000)                 # append 100000
num.sort(reverse=True)             # sort.(reverse) the appended list orderly
print(f"{num.reverse()}, {num}")   # just reverse the list
print(type(num))
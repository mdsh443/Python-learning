#append() => list mutate korte help kore. Ekhane .append() function er value
# list er last a add hobe.
# list method ke print korle output always NONE ashe.
list = [2, 99, 4, 66]
list.append(10)
print(list.append(11)) # output => None
print(list)

#sort() => list ke ascending or descending order a rearrange kore.
#ascending order:
list_1 = [2, 67383, 36, 1, 2222]
#list_1.append(10)
#list_1.sort()
#print(list_1)
print(list_1.append(10))
print(list_1.sort())
# print(list_1.sort(reverse=True))
print(list_1)

# descending order:
list_2 = [2, 67383, 36, 1, 2222]
#list_2.append(10)
#list_2.sort()
#print(list_2)
# print(list_2.append(10))
# print(list_2.sort())
print(list_2.sort(reverse=True))
print(list_2)

#string: string sorting korle a, b, c, d.... eibhabe ascending
# and z,y,x....... decending order a sort hoi.
alphabet = ["a", "b", "c", "d", "y"]
alphabet.append("z")
# alphabet.sort()
alphabet.sort(reverse=True)
print(alphabet)

#another string example:
fruit = ["apple", "banana", "mango"]
fruit.append("berry")
fruit.sort(reverse=True)
print(fruit) # output=> ['mango', 'berry', 'banana', 'apple'] because mango comes first
             # the berry then banana, then apple.   


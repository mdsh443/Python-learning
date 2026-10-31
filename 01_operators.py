a = 5 
b = 2
c = float(a/b)
d = (a!=b)
e = (a == b)
print(a+b)
print(c)
print(a%b)
print(a**b)

print(d)
print(e) 

#assignment operators
num = 100
num = num + 10
print(num)

dum = 10
dum -= 1
print(dum)

gum = 2
gum **= 3
print(gum)

#Logical operators:
q = 50
p = 30
print(not False)
print(not True)

print(not (a<b))
print(not (a>b))

val_1 = True
val_2 = False

print(f"'and' operator: {val_1 and val_2}")
print(f"'OR' operator: {val_1 or val_2}")

f = 10
g = 11

""" AND operator ekmatro jokhon 2 ta condition True hobe tokhon e ans True hobe
otherwise always False ans hobe. je kono ekta condition False holei AND operator 
False ans dibe. Check example """

print(f"'AND' operator: {(f==g) and (f!=g)}")
print(f"'AND' operator: {(f==g) and (f==g)}")
print(f"'AND' operator: {(f!=g) and (f!=g)}")
print(f"AND: {(f>g) and (f<g)}")

""" OR operator ekmatro jokhon 2 ta condition False hobe tokhon e ans False hobe
otherwise always True ans hobe. je kono ekta condition True holei OR operator 
True ans dibe. Check example """

print(f"'OR' operator: {(f==g) or (f!=g)}")
print(f"'OR' operator: {(f==g) or (f==g)}")
print(f"OR: {(f>g) or (f<g)}")
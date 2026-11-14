# Loops are used to repeat instructions. 

#while loop: (in Bangla): while => যতক্ষণ
# 2 types of loops: for loops and while loops
# Never create a infinite loop. That means always pick a condition that will become 
# False at some point of the loop repeatation.

i = 1
while i <= 5:    # joto-khon ei condition true thakbe totokhon loop cholte thakbe.
                 # here i is counter variable and each round is called iteration.
    print("Lisan Al Gaib")
    i += 1       # detail: (i = i + 1)
print(i)


count = 5
while count >= 1:
    print(count)
    count -= 1
print(count)
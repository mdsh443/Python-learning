
# tuple is immutable. can not assign other value like list in tuple.
# list a amra [] use kori. Tuple amra () use kori to store values.
tup = (2, 1, 3 ,1)
print(type(tup))
print(tup[0])
print(tup[2])
print(tup)

# single element tuple er last a ekta , mandatory. Otherwise eta integer hoye jabe.
# multiple element tuple er last a , mandatory na but dile kono problem nai.
tup1 = (1,)
tup2 = ("mango",)
tup3 = ("alice", "nawaz", "joshim", "rinthy", "adam",)
print(type(tup1))
print(type(tup2))
print(type(tup3))
print(tup3)

tup4 = (2, 1, 3 , 1, 100, 200, 300,)
print(tup[1:5])
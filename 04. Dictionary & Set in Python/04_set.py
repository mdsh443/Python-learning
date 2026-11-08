# Set is the collection of unordered items.
# Each element in the set must be unique and immutable.
# boolean, integer, float, string, tuple ===> immutable.
# list, dictionary ===> mutable.
print("\nStart of the program\n")

num = {1, 1, 2, 3, 3, 4, "hello", "hello", "world"} #set ignores duplicate values
print(num)       # output=> {1, 'hello', 2, 3, 4, 'world'} => unordered
print(type(num))
print(len(num))

print("\nEnd of the program\n")

collection_1 = {}  # this is not an empty set, this is an empty dictionary
print(type(collection_1))

collection = set()  # this is an empty set
print(type(collection))

print("\nEnd of the program\n")


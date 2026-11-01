string = "Hello world"
# character = string[3]
# print(character)  ##### [E bhabeo solve kora jeto]

# Character count always 0 theke shuru hobe not 1 theke for positive counting.
# like "Hello World" => 012345678910. Counting start hobe left to right =>.
print(string)
print(f"Character no. 4: {string[4]}")
print(f"Character no. 8: {string[8]}")

# Slicing:
name = "md shahnaouz"
print(f"Sliced character: {name[1:7]}")
print(f"Sliced character: {name[3:]}")
print(f"Sliced character: {name[3:len(name)]}")
print(f"Sliced character: {name[3:7]}")

# Character count always -1 theke shuru hobe not 0 or 1 theke for negative counting.
# like "Hello World" => -1-2-3-4-5-6-7-8-9-10-11. Counting start hobe right to left <=.
fruit = "apple"
print(f"$liced character: {fruit[-4:-1]}")
print(f"$liced character: {fruit[-3:-1]}")


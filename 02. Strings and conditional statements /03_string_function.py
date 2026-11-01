
# str.endswith() function: kono long string er moddhe ekta choto sub-string,
# like a small part of a string find korar jonno endswith() use kora hoi:
str = "i am a coder and learning python now"
print(str.endswith("now"))
print(str.endswith("app"))

# name.capitalize() function: kono long string er first letter ke just capitalize kore dei. 
name = "my name is shahnaouz & i am learning python"
print(f"Capitalized string: {name.capitalize()}")
print(f"Normal output: {name}\n")

# rep.replace() function: string er moddhe kono letter or word ke replace kore replace() function:
rep = "i am a coder and learning python now"
print(f"Replaced string: {rep.replace("a", "@")}")
print(f"Replaced string: {rep.replace("python", "java-script")}\n")

# str_1.find() function: string er moddhe kono letter or word ke find korte use hoi find() function:
# eta string er index ke count kore. for example:
str_1 = "i am a coder and learning python now"
print(f"Find the letter: {str_1.find("a")}")
print(f"Find the word: {str_1.find("now")}\n")

# str_2.count() function:
str_2 = "i am a coder and learning python and it's going pretty good"
print(f"Count the letter: {str_2.count("a")}")
print(f"Count the word: {str_2.count("and")}\n")


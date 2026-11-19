# For Loop:

# A for loop goes through items one at a time by following a sequence. 
# This is what “sequential traversal” means. 
# Unlike the counter-based while loop, you do not need to increase a counter yourself. 
# The for loop automatically moves to the next item and stops when no items remain.

# devices = ["Router", "Switch", "Firewall"]

# for device in devices:
#     print(device)

# Output =>
#     Router
#     Switch
#     Firewall

# “For each item in devices, put that item into device and run the indented instructions.”

# A for loop lets you write the printing instruction once, then apply it to every item.

# for - Starts the loop.
# device - A variable that holds the current item.
# in devices - Take the items from the list named devices
# :   -  The instructions belonging to the loop come next.

# device and devices are different variables.
# devices holds the whole list.
# device holds one item at a time.

# You do not need to create device before the loop. Python assigns an item to it when each repetition begins.
# When there are no more items left in devices, so the loop finishes. Each repetition is called an iteration.
# The variable name is your choice. Python does not require the name device. This also works:

# devices = ["Router", "Switch", "Firewall"]
#
# for item in devices:
#     print(item)



devices = ["Router", "Switch", "Firewall"]

for item in devices:
    print(f"{item} is ready")
    
# 
devices_1 = ["Router", "Switch", "Firewall"]

for device in devices_1:
    print(f"{device} is standby")
    
#    
nums = [1, 2, 3, 4, 5]

for value in nums:
    print(value)
    
# 
vegetables = ["potato", "tomato", "cucumber", "eggplants"]

for veg in vegetables:
    print(veg)
    
# 
tup = (1, 2, 3, 4, 5,)

for num in tup:
    print(num)

# 
name = "Mdshahnaouz"

for alph in name:
    if (alph == "o"):
        print("o is found")
        break
    print(alph)
        
else:
    print("END")
    
# How for ... else works:
#  break immediately stops the loop.
#  The loop’s else runs only if the loop finishes without break.
# Your string contains "o", so Python prints "o is found" and stops the loop. 
# It skips else, then runs the final print(alph)
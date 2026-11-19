# My Python Learning Journey

My name is Md Shahnaouz. I am learning Python to prepare
for my KTH studies and develop my computer networking skills.

## Topics Practised

- Variables and data types
- Input and output
- Strings and string methods
- Operators and conditional statements
- Loops
- Lists and tuples
- Dictionaries and sets
- Basic client-server communication using sockets

## Repository Contents

This repository contains my lesson notes, exercises,
and small Python programs.

## Current Goal

Practise the fundamentals and write networking-related
programs independently.

















## The 3 Golden Rules of Every while Loop
If you want to write or understand a while loop easily, always look for these three components:

- Initialization: Setting a starting value before the loop starts (e.g., router = 1).  
- The Condition: The rule that decides whether the loop keeps running or stops (e.g., router <= 3). 
- The Updater: A line inside the loop that changes your variable so the condition eventually 
               becomes False (e.g., router += 1 or router -= 1). Without this, you get an infinite loop
               that runs forever and can freeze your program!






  For Loop:

A for loop goes through items one at a time by following a sequence. This is what “sequential traversal” means. Unlike the counter-based while loop, you do not need to increase a counter yourself. The for loop automatically moves to the next item and stops when no items remain.

devices = ["Router", "Switch", "Firewall"]

for device in devices:
    print(device)

Output =>
    Router
    Switch
    Firewall

“For each item in devices, put that item into device and run the indented instructions.”

A for loop lets you write the printing instruction once, then apply it to every item.

for - Starts the loop.
device - A variable that holds the current item.
in devices - Take the items from the list named devices
:   -  The instructions belonging to the loop come next.
device and devices are different variables.
devices holds the whole list.
device holds one item at a time.
You do not need to create device before the loop. Python assigns an item to it when each repetition begins.
When there are no more items left in devices, so the loop finishes. Each repetition is called an iteration.
The variable name is your choice. Python does not require the name device. This also works:
devices = ["Router", "Switch", "Firewall"]
for item in devices:
    print(item)
Output =>
    Router
    Switch
    Firewall

You can use a for loop with lists, tuples, strings, dictionaries, sets, and range().
These are iterable: Python can take items from them one at a time.
Type
Example
What the loop takes each time
List
["Router", "Switch"]
One item
Tuple
("Router", "Switch")
One item
String
"Router"
One character
Diction ary


{
"name": "Router", 
"status": "up"
}
One key, by default

Set

{"Router", "Switch"}

One unique item; order is not guaranteed
range()
   range(1, 4)
One integer: 1, then 2, then 3





Use a for loop to process items one at a time. Use a while loop to repeat instructions while a condition is true.

Situation
Usual choice
Print every device in a list 
for
Examine every character in a string
for
Repeat an instruction five times
for with range()
Keep asking for input until it is valid
while
Keep showing a menu until the user chooses “Exit”
while


Both loop types can sometimes solve the same task. Choose the one that expresses your intention clearly:
for: “For each item, do this.”
while: “As long as this condition is true, keep doing this.”

We use else in a for loop when we want something to happen only if the loop finishes without break.
devices = ["Router", "Switch", "Firewall"]
for device in devices:
    if device == "Server":
        print("Server found")
        break
else:
    print("Server not found")

Here is what happens:
Check "Router" — not "Server".
Check "Switch" — not "Server".
Check "Firewall" — not "Server".
No items remain, and break never ran.
The else prints:
               Server not found
Outside the loop, that statement would run even if the server was found. Attaching it to else makes it run only when the search finishes without break.
Notice that else lines up with for, because it belongs to the loop.
A loop’s else runs when the loop finishes without break.


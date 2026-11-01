
age = int(input("Enter your age: ")) 
if (age >= 18):
    print("\ncan vote & apply for license\n")
    print("can drive car\n") 
else:
    print("can't vote")
    
##############################    
light = input("Enter light color: ") 
# light = "green"                  # hard coded value diyeo kora jeto.
if (light == "green"):
    print("drive")                 # ekta program a onek gulo if statement thakte pare independently. 
elif (light == "yellow"):          # But elif statement always ekta  if statement er under a thakbe not 
    print("look")                  # independently thakbe.
elif (light == "red"):             # else statement just ektai thakbe program er last a.
    print("stop") 
else:
    print("traffic light is broken")

print("End of program\n")
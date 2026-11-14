#Q.1: write a small program using a while loop to produce:
# Checking router 1
# Checking router 2
# Checking router 3
# All routers checked

# Answer:

router = 1
while router <= 3:
    print(f"Checking router {router}")
    router += 1

print("All routers checked")

#Q.2: write a small program using a while loop to produce:
# Checking router 3
# Checking router 2
# Checking router 1
# All routers checked

# Answer:

router = 3
while router >= 1:
    print(f"Checking router: {router}")
    router -= 1

print("All routers checked")
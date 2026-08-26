while ((shining := input("Is the sun shining (yes/no): ")) != "yes" and shining != "no"):
    print("Enter a valid answer")

while not (0 <= (time := int(input("Enter current time: "))) <= 23):
    print("Enter a valid time as integer")

if shining and (10 <= time <= 16):
    print("Please use sunscreen")
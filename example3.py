while not (1 <= (day := int(input("Give day of week (1-7): "))) <= 7):
    print("Enter a valid day (1-7)")

while ((vacation := input("On vacation (yes/no): ")) != "yes" and vacation != "no"):
    print("Give a valid answer")

if day >= 6 or vacation == "yes":
    sleep_late = True
else:
    sleep_late = False
print(sleep_late)
year = int(input("Enter a year: "))

# 1
is_leap = False
if year % 4 == 0:
    is_leap = True

if year % 100 == 0:
    is_leap = False

if year % 400 == 0:
    is_leap = True

print(f"{year} is a leap year: {is_leap}")

# 2
is_leap = False
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    is_leap = True
else:
    is_leap = False

print(f"{year} is a leap year: {is_leap}")
# 1
for n in range(1, 101):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1

    if n == i:
        print(n, end=" ")
print()

# 2
count = 0
n = 1
while count < 100:
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1

    if n == i:
        print(n, end=" ")
        count += 1
    n += 1
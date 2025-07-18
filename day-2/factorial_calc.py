n = int(input("Enter the number: "))
prod = 1
while n > 0:
    if n == 1:
        print(f"{n} =", end="")
        n -= 1
    else:
        print(f"{n} *", end="")
        prod *= n
        n -= 1
print(prod)
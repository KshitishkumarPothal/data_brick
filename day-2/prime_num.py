n = int(input("Enter the number you want to check: "))

count = 0
for i in range(1,n//2 + 1):
    if (n % i) == 0:
        count += 1
if count == 1:
    print("Its a prime")
else:
    print("Its a consonant")
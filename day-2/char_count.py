s = input("Enter a string: ")

k = input("Enter the char you want to count in above string : ")

if k in s:
    print(s.count(k))
else:
    print("Not found")
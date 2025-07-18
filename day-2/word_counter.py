s = input("Enter a sentence")
n = input("Enter a word you want to check")

if n in s:
    print(s.count(n))
else:
    print("Not fornd")
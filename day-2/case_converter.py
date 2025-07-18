s = input("Enter a string")
ans = ""
for i in range(len(s)):
    if s[i].isalpha():
        if s[i].isupper():
            ans += s[i].lower()
        else:
            ans += s[i].upper()
print(ans)
n = float(input("Enter the percentage: "))

if n >= 90:
    print("Grade is O")
elif n >= 80 and n < 90:
    print("Grade is E")
elif n >= 70 and n < 80:
    print("Grade is A")
elif n >= 60 and n < 70:
    print("Grade is B")
elif n >= 50 and n < 60:
    print("Grade is C")
elif n >= 33 and n < 50:
    print("Grade is D")
elif n < 33:
    print("You are fail")
else:
    print("Enter a valid number")
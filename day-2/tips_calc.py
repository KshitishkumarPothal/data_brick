n = int(input("Enter the amount paid by customer: "))
s = int(input("Enter the total bill of customer: "))
if n > s:
   print(f"The tips paid by customer is {n - s}")
else:
   print("The customer cheet you")
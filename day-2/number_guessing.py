import random

n = random.randint(1,10)
# l = [1,2,3,4,5,6,7,8,9,10]
# m = random.choice(l)
# print(m)
k = int(input("Enter a number between 1 to 10: "))

win = False
while not win:
    if n == k:
      print("You are correct")
      win = True
    elif n < k:
       k = int(input("Guess the number less then you guess: "))
    else:
       k  = int(input("Number is greter then this: "))


# print(n)
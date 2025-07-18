a = "Kshitish"
b = 22
msg = "hello i am {} and i am {} years old".format(a,b)
print(msg)


name = "kshitish"
age = 23
print(f"hello i am {name} and i am {age} years old")

def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)
print(facto(5))
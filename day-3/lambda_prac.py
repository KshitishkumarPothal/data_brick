sq = lambda x : x**2
print(sq(4))

n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(0))
print(n(10))

s1 = "kshitishkumarpothal"
s2 = lambda s: s.upper()
print(s2(s1))

li = [lambda args = x : args * 10 for x in range(1, 10)]
for i in li:
    print(i())


calc = lambda x,y : (x+y , x*y)
print(calc(2,4))

l = [2,3,4,5,6,7]
even = filter(lambda x: x%2 == 0,l)
print(list(even))


from functools import reduce

a = [1,2,3,4]
b = reduce(lambda x,y : x*y, a)
print(b)

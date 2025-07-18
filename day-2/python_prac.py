
a = {1,2,"ksh"}
b = frozenset([1,2,3])
b.add(4)
print(b)

l1 = [1,1,1,2,3,4]
l1.append(5)
# l1.add(9)
l1.insert(4,7)
print(l1)
l1.remove(2)
print(l1)
l1.pop()
print(l1)
l1.extend([7,8,9])
print(l1)
print(l1.index(4))
print(l1.count(1))

s1 = {1,2,3,4}
s1.add(5)
# l1.add(9)
print(s1)
s1.remove(2)
print(s1)
s1.pop()
print(s1)
# s1.extend({7,8,9})
# print(s1)
print(s1.isdisjoint({1,4,6}))
# print(s1.count(1))


d1 = {"a":1,"b":2, "c":3,"d":4}
d1.pop("b")
d1["k"] = 19
d1.popitem()
print(d1)
t1= (1,2,3,4)
print(t1.index(3))




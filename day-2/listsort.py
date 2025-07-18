a = [1,5,4,3,5,7,8,9]
b = [1,5,4,3,5,7,8,9]

print(sorted(a))
b.sort()
print(b)

# bubble sort

c = [1,5,4,3,5,7,8,9]
for i in range(len(c)):
    for j in range(0,len(c)-i - 1):
        if c[j] > c[j+1]:
            c[j],c[j+1] = c[j+1],c[j]
print(c)

#selection sort
d = [1,5,4,3,5,7,8,9]
n = len(d)
for i in range(n):
    min_idx = i
    for j in range(i + 1,n):
        if d[j] < d[min_idx]:
            min_idx = j
    d[i],d[min_idx] = d[min_idx],d[i]
print(d)

#insertion sort
e = [1,5,4,3,5,7,8,9]
n = len(e)
for i in range(1,n):
    k = e[i]
    j = i-1
    while j >= 0 and k < c[j]:
        c[j+1] = c[j]
        j -= 1
    c[j+1] = k
print(e)

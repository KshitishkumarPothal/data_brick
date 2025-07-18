from collections import deque

dp = deque([1,2,3])
dp.append(4)
dp.appendleft(0)
print(dp)
dp.pop()
print(dp)
dp.popleft()
print(dp)
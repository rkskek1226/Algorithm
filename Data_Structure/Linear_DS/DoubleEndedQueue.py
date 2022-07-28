from collections import deque

dq = deque()
dq.append(0)
dq.append(1)
dq.append(2)
dq.appendleft(-1)
dq.appendleft(-2)

for i in dq:
    print(i, end=" ")
print()

dq.pop()
for i in dq:
    print(i, end=" ")
print()

dq.popleft()
for i in dq:
    print(i, end=" ")
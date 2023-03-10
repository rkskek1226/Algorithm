import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for _ in range(n):
    tmp = sys.stdin.readline().split()

    if tmp[0] == "push_front":
        d.appendleft(tmp[1])
    elif tmp[0] == "push_back":
        d.append(tmp[1])
    elif tmp[0] == "pop_front":
        if not d:
            print("-1")
        else:
            print(d.popleft())
    elif tmp[0] == "pop_back":
        if not d:
            print("-1")
        else:
            print(d.pop())
    elif tmp[0] == "size":
        print(len(d))
    elif tmp[0] == "empty":
        if not d:
            print("1")
        else:
            print("0")
    elif tmp[0] == "front":
        if not d:
            print("-1")
        else:
            print(d[0])
    elif tmp[0] == "back":
        if not d:
            print("-1")
        else:
            print(d[-1])


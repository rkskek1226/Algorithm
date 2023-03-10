import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    result = ""
    d = deque()
    _ = int(sys.stdin.readline())
    s = sys.stdin.readline().strip().replace(" ", "")
    d.append(s[0])

    for i in range(1, len(s)):
        if ord(s[i]) <= ord(d[0]):
            d.appendleft(s[i])
        else:
            d.append(s[i])

    print("".join(d))

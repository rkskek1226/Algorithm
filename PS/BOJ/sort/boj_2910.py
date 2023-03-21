import sys
from collections import Counter


n, c = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
x = []
counter = Counter(l)

for i in l:
    x.append([i, counter[i], l.index(i)])

x.sort(key=lambda x: (-x[1], x[2]))

for i in x:
    print(i[0], end=" ")

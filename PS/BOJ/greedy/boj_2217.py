import sys

n = int(sys.stdin.readline().strip())
l = []

for _ in range(n):
    l.append(int(sys.stdin.readline().strip()))

l.sort(reverse=True)
tmp = []

for i in range(len(l)):
    tmp.append(l[i] * (i + 1))

print(max(tmp))

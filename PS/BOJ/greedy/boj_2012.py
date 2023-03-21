import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(int(sys.stdin.readline().strip()))

l.sort()
result = 0

for i in range(len(l)):
    result += abs((i + 1) - l[i])

print(result)

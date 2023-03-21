import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
tmp = 0

for i in range(len(l)):
    tmp += sum(l[:i + 1])

print(tmp)

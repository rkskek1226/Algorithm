import sys

n, start = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

for i in arr:
    if start >= i:
        start += 1
    else:
        break

print(start)

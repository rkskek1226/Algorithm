import sys

n, m = map(int, sys.stdin.readline().split())
result = "Yes"

for i in range(m):
    tmp = sys.stdin.readline()
    data = list(map(int, sys.stdin.readline().split()))

    if data != sorted(data, reverse=True):
        result = "No"
        break

print(result)

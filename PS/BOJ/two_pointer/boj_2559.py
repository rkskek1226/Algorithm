import sys

n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
left = 1
tmp = [sum(l[:k])]

while left <= n - k:
    tmp.append(tmp[-1] - l[left - 1] + l[left + k - 1])
    left += 1

print(max(tmp))

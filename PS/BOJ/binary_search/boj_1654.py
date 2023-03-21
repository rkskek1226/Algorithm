import sys

k, n = map(int, sys.stdin.readline().split())
l = []

for _ in range(k):
    l.append(int(sys.stdin.readline().strip()))

l.sort()

left, right = 1, sum(l) // n
hap = 0

while left <= right:
    mid = (left + right) // 2
    hap = 0

    for i in l:
        hap += i // mid

    if hap >= n:
        left = mid + 1
    elif hap < n:
        right = mid - 1

print(right)


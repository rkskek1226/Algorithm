import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l.sort()

left, right = 0, max(l)

while left <= right:
    mid = (left + right) // 2
    hap = 0

    for i in l:
        if i > mid:
            hap += (i - mid)

    if hap < m:
        right = mid - 1
    elif hap >= m:
        left = mid + 1

print(right)

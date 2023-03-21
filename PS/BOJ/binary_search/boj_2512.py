import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

l.sort()
left, right = 0, max(l)

if sum(l) <= m:
    print(max(l))
else:
    while left <= right:
        hap = 0
        mid = (left + right) // 2

        for i in l:
            if mid >= i:
                hap += i
            else:
                hap += mid

        if hap <= m:
            left = mid + 1
        elif hap > m:
            right = mid - 1
    print(right)


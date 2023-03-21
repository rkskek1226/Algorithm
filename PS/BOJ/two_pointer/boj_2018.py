import sys

n = int(sys.stdin.readline().strip())
left, right = 0, 0
cnt, hap = 0, 0

while left <= right and right <= n:
    if hap == n:
        cnt += 1
        right += 1
        hap += right
    elif hap > n:
        hap -= left
        left += 1
    else:
        right += 1
        hap += right

print(cnt)

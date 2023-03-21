import sys

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())

l.sort()
cnt = 0
left, right = 0, len(l) - 1

while left < right:
    if l[left] + l[right] == x:
        cnt += 1
        left += 1
    elif l[left] + l[right] < x:
        left += 1
    else:
        right -= 1

print(cnt)




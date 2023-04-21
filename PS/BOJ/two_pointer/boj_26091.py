import sys

N, M = map(int, sys.stdin.readline().split())
members = list(map(int, sys.stdin.readline().rstrip().split()))
members.sort()

cnt = 0
left, right = 0, len(members) - 1

while left <= right and right - left != 0:
    if members[left] + members[right] >= M:
        cnt += 1
        left += 1
        right -= 1
    elif members[left] + members[right] < M:
        left += 1

print(cnt)


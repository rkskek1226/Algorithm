import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
answer = 0

left, right = 0, len(arr) - 1

while left < right:
    if arr[left] + arr[right] >= m:
        answer += 1
        left += 1
        right -= 1
    else:
        left += 1

print(answer)
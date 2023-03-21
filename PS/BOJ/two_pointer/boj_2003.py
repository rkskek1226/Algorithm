import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
cnt = 0
left, right = 0, 0

while right < n and left <= right:
    hap = sum(l[left:right + 1])

    if hap == m:
        cnt += 1
        right += 1
    elif hap < m:
        right += 1
    else:
        if left == right:   # 입력이 1, 2, 3, 1일때 left, right가 2에서 만남
            right += 1
        else:
            left += 1

print(cnt)

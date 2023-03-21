import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
test_n = int(sys.stdin.readline())
test_case = list(map(int, sys.stdin.readline().split()))

l.sort()

for target in test_case:
    left, right = 0, len(l) - 1
    flag = False

    while left <= right:
        mid = (left + right) // 2

        if l[mid] < target:
            left = mid + 1
        elif l[mid] > target:
            right = mid - 1
        else:
            flag = True
            break

    if flag:
        print(1)
    else:
        print(0)


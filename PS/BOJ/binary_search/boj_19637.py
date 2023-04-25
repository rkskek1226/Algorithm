import sys
import collections


N, M = map(int, sys.stdin.readline().rstrip().split())

list_a = []
list_b = []


def binary_search(list_a, list_b, target):
    left = 0
    right = len(list_b) - 1

    while left <= right:
        mid = (left + right) // 2

        if list_b[mid] < target:
            left = mid + 1
        elif list_b[mid] >= target:
            right = mid - 1
    return list_a[right + 1]


for _ in range(N):
    tmp = list(sys.stdin.readline().split())

    if list_b and tmp[1] == list_b[-1]:
        continue
    list_a.append(tmp[0])
    list_b.append(int(tmp[1]))


for _ in range(M):
    print(binary_search(list_a, list_b, int(sys.stdin.readline())))


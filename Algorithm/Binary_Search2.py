import sys
from typing import *


# 이진 탐색
# 1. 반복 풀이
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1


# 정렬된 배열에서 특정 수의 개수 구하기
def q1():
    N, x = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    answer1, answer2 = -1, -1

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            answer1 = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            answer2 = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    if answer1 == -1 and answer2 == -1:
        print(-1)
    elif answer1 != -1 and answer1 == answer2:
        print(1)
    else:
        print(answer2 - answer1 + 1)


# 고정점 찾기
def q2():
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    left, right = 0, len(arr) - 1
    flag = False

    while left <= right:
        mid = (left + right) // 2

        if mid == arr[mid]:
            flag = True
            break
        elif mid < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if flag:
        print(mid)
    else:
        print(-1)
        


q2()
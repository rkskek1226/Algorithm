import bisect
import sys


# bisect 라이브러리는 정렬된 리스트에서 특정 원소를 찾을 때 효과적
# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 리턴
# bisect_right(a, x) : 정렬된 순서를 유지하면 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 리턴
# bisect_left()와 bisect_right()는 O(logN)


arr = [0, 1, 2, 3, 4, 5]
print(bisect.bisect_left(arr, 2))   # 2 리턴
print(bisect.bisect_right(arr, 3))   # 4 리턴

arr = [1, 2, 4, 4, 8]
print(bisect.bisect_left(arr, 4))   # 2 리턴
print(bisect.bisect_right(arr, 4))   # 4 리턴


# bisect_left()와 bisect_right()를 활용하면 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 효과적으로 구할 수 있음
def count_by_range(a, left_value, right_value):
    right_idx = bisect.bisect_right(a, right_value)
    left_idx = bisect.bisect_left(a, left_value)
    return right_idx - left_idx


a = [1, 2, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))   # 값이 4인 데이터 개수 출력
print(count_by_range(a, -1, 3))   # 값이 -1 ~ 3 범위에 있는 개수 출력



# 부품 찾기
def q1():
    N = int(sys.stdin.readline().rstrip())
    arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

    arr1.sort()

    print(arr1, "\n", arr2)
    for target in arr2:
        left, right = 0, len(arr1) - 1
        flag = False

        while left <= right:
            mid = (left + right) // 2

            if arr1[mid] == target:
                flag = True
                break
            elif arr1[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if flag:
            print("yes")
        else:
            print("no")


# 떡볶이 떡 만들기
def q2():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort()
    answer = 0

    left, right = 0, max(arr)

    while left <= right:
        mid = (left + right) // 2
        hap = 0

        for i in arr:
            if i > mid:
                hap += (i - mid)

        if hap < M:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    print(left)


q2()
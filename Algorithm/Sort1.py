import sys
import collections


# 성적이 낮은 순서로 학생 출력하기
def q1():
    N = int(sys.stdin.readline().rstrip())
    arr = []
    for _ in range(N):
        arr.append(list(sys.stdin.readline().rstrip().split()))

    print(arr)
    arr.sort(key=lambda x: int(x[1]))
    
    for i in arr:
        print(i[0], end=" ")


# 두 배열의 원소 교체
def q2():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
    arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

    arr1.sort()
    arr2.sort()

    arr1 = collections.deque(arr1)
    arr2 = collections.deque(arr2)

    for _ in range(K):
        if arr1[0] < arr2[-1]:
            arr1.popleft()
            arr1.append(arr2.pop())

    print(sum(arr1))



q2()
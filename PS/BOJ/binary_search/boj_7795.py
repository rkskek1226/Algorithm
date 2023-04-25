# 못 품
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    _ = sys.stdin.readline()
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))

    A = list(set(A))
    B = list(set(B))

    A.sort()
    B.sort()
    cnt = 0

    for i in A:
        left, right = 0, len(B) - 1

        while left <= right:
            mid = (left + right) // 2

            if B[mid] < i:
                left = mid + 1
            elif B[mid] >= i:
                right = mid - 1

        cnt += (right + 1)

    print(cnt)



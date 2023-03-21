import sys

test_n = int(sys.stdin.readline().rstrip())
test_case = []

for _ in range(test_n):
    _ = sys.stdin.readline()
    result = 0
    test_case = list(map(int, sys.stdin.readline().split()))
    m = 0

    for j in range(len(test_case) - 1, -1, -1):
        if test_case[j] >= m:
            m = test_case[j]
        else:
            result += (m - test_case[j])

    print(result)

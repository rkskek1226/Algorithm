import sys

test_n = int(sys.stdin.readline())

for _ in range(test_n):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apt = [i for i in range(1, n + 1)]   # 0 floor

    for i in range(k):
        for j in range(1, n):
            apt[j] += apt[j - 1]

    print(apt[-1])


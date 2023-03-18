import sys
sys.setrecursionlimit(10**9)


def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return

    if graph[i][j] == 1:
        graph[i][j] = 0

        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)


test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)


import sys
from collections import deque


def bfs(v, n):
    queue = deque([v])
    discovered = []
    cnt = [0] * (n + 1)
    cnt[v] = 1

    while queue:
        i = queue.popleft()

        for j in graph[i]:
            if cnt[j] == 0:
                queue.append(j)
                cnt[j] = cnt[i] + 1

    return cnt


n, m = map(int, sys.stdin.readline().split())
graph = {}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph.keys():
        graph[b].append(a)
    else:
        graph[b] = [a]

result = bfs(1, n)
print(result.index(max(result)), max(result) - 1, result.count(max(result)), sep=" ")

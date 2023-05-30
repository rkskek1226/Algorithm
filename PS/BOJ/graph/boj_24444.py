import sys
import collections

N, M, R = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
visited = [0] * (N + 1)
visited[R] = 1
q = collections.deque([R])
cnt = 1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

while q:
    v = q.popleft()

    for i in graph[v]:
        if visited[i] == 0:
            q.append(i)
            cnt += 1
            visited[i] = cnt

for i in visited[1:]:
    print(i)

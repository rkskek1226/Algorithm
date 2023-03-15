import sys
import heapq
from collections import defaultdict


n, m, k, x = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
dist = defaultdict(int)
q = [(0, x)]   # [w, v] 구조

for _ in range(m):
    a, v = map(int, sys.stdin.readline().split())
    graph[a].append((1, v))

while q:
    time, node = heapq.heappop(q)

    if node not in dist:
        dist[node] = time
        for w, v in graph[node]:
            heapq.heappush(q, (time + w, v))

if k not in dist.values():
    print(-1)
else:
    for key in dist.keys():
        if dist[key] == k:
            print(key)

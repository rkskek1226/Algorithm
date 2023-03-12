import sys


def bfs(graph, start_v):
    discovered = [start_v]
    queue = [start_v]
    cnt = 0

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
                cnt += 1

    return cnt


test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):
    _, n = map(int, sys.stdin.readline().split())

    graph = {}
    start_v = -1

    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if i == 0:
            start_v = a

        if a in graph.keys():
            graph[a].append(b)
        else:
            graph[a] = [b]

        if b in graph.keys():
            graph[b].append(a)
        else:
            graph[b] = [a]

    print(bfs(graph, start_v))


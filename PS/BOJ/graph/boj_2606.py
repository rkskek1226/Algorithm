import sys


def dfs(v, discovered=[]):
    if v not in discovered:
        discovered.append(v)

    for i in graph[v]:
        if i not in discovered:
            discovered = dfs(i, discovered)

    return discovered


computer_n = int(sys.stdin.readline())
pair_n = int(sys.stdin.readline())
graph = {}

for _ in range(pair_n):
    a, b = map(int, sys.stdin.readline().split())

    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph.keys():
        graph[b].append(a)
    else:
        graph[b] = [a]

print(len(dfs(1, [])) - 1)

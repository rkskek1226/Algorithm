from queue import Queue


class Graph:
    def __init__(self, vertex_num):
        self.list = [[] for _ in range(vertex_num)]
        self.visited = [False for _ in range(vertex_num)]

    def add_edge(self, u, v):
        self.list[u].append(v)
        self.list[v].append(u)

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False

    def bfs(self, v):
        q = Queue()

        q.put(v)
        self.visited[v] = True

        while not q.empty():
            v = q.get()
            print(v, end=" ")

            adj_v = self.list[v]

            for u in adj_v:
                if not self.visited[u]:
                    q.put(u)
                    self.visited[u] = True

    def dfs(self, v):
        print(v, end=" ")

        self.visited[v] = True

        adj_v = self.list[v]
        for u in adj_v:
            if not self.visited[u]:
                self.dfs(u)


def recursive_dfs(v, discovered=[]):
    discovered.append(v)

    for i in graph[v]:
        if i not in discovered:
            discovered = recursive_dfs(i, discovered)
    return discovered


def stack_dfs(start_v):
    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.append(v)

            for i in graph[v]:
                stack.append(i)

    return discovered


def queue_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

print(recursive_dfs(1))
print(stack_dfs(1))
print(queue_bfs(1))



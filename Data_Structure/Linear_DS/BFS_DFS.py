from queue import Queue
import Stack

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








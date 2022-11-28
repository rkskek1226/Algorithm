class Graph:
    def __init__(self, vertex_num=None):
        self.list = []
        self.vtx_num = 0
        self.vtx_arr = []

        if vertex_num:
            self.vtx_num = vertex_num
            self.vtx_arr = [True for _ in range(self.vtx_num)]
            self.list = [[] for _ in range(self.vtx_num)]

    def is_empty(self):
        if self.vtx_num == 0:
            return True
        else:
            return False

    def add_vertex(self):
        for i in range(len(self.vtx_arr)):
            if self.vtx_arr[i] == False:  # vtx_arr[i]가 False면 삭제된 노드라는 의미
                self.vtx_num += 1
                self.vtx_arr[i] = True
                return i
        self.list.append([])
        self.vtx_num += 1
        self.vtx_arr.append(True)
        return self.vtx_num - 1

    def delete_vertex(self, v):
        if v >= self.vtx_num:
            raise Exception("There is no vertex of {}".format(v))

        if self.vtx_arr[v]:
            self.list[v] = []
            self.vtx_num -= 1
            self.vtx_arr[v] = False

            for adj in self.list:
                if v in adj:
                    adj.remove(v)

    def add_edge(self, u, v):
        self.list[u].append(v)
        self.list[v].append(u)

    def delete_edge(self, u, v):
        self.list[u].remove(v)
        self.list[v].remove(u)

    def show(self):
        for i in range(len(self.list)):
            print("{} : ".format(i), end=" ")
            for vertex in self.list[i]:
                print("{}".format(vertex), end=" ")
            print()


g = Graph()
g.add_vertex()
g.add_vertex()
g.add_vertex()
g.add_vertex()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(0, 3)
g.show()
print()
g.delete_vertex(1)
g.show()
print()
g.add_vertex()
g.add_edge(0, 1)
g.show()



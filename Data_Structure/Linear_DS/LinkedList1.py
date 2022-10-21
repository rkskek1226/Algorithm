# 연결 리스트의 탐색 : O(n)
# 연결 리스트의 시작, 끝에 삽입, 삭제, 추출은 O(1)

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self._data = data
        self._prev = prev
        self._next = next

    def __del__(self):
        print("data {} is deleted".format(self.data))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self._prev = prev

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def size(self):
        return self.size

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.size += 1

    def insert_after(self, data, node):
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next

        node.next.prev = new_node
        node.next = new_node

        self.size += 1

    def insert_before(self, data, node):
        new_node = Node(data)
        new_node.prev = node.prev
        new_node.next = node

        node.prev.next = new_node
        node.prev = new_node

        self.size += 1

    def search_forward(self, target):
        cur = self.head.next

        while cur is not self.tail:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def search_backward(self, target):
        cur = self.tail.prev

        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.prev
        return None

    def show_forward(self):
        cur = self.head.next

        while cur is not self.tail:
            print(cur.data, end=" ")
            cur = cur.next

        print("")

    def show_backward(self):
        cur = self.tail.prev

        while cur is not self.head:
            print(cur.data, end=" ")
            cur = cur.prev

        print()

    def delete_first(self):
        if self.is_empty():
            return False

        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.size -= 1

    def delete_last(self):
        if self.is_empty():
            return False

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.size -= 1

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1


dl = DoubleLinkedList()
print("1 삽입")
dl.add_first(1)
dl.show_forward()
print("2 삽입")
dl.insert_after(2, dl.search_forward(1))
dl.show_forward()
print("3 삽입")
dl.insert_after(3, dl.search_forward(2))
dl.show_forward()
print("5 삽입")
dl.add_last(5)
dl.show_forward()
print("4 삽입")
dl.insert_before(4, dl.search_backward(5))
dl.show_forward()
dl.show_backward()

print("1 삭제")
dl.delete_first()
dl.show_forward()
print("5 삭제")
dl.delete_last()
dl.show_forward()
dl.show_backward()
print("3 삭제")
dl.delete_node(dl.search_forward(3))
print(dl.show_forward())
print(dl.show_backward())

print("finish\n\n")





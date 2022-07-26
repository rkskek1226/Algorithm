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
        self.head = Node()
        self.tail = Node()

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
        pass

    def insert_before(self, data, node):
        pass

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

    def delete_first(self):
        pass

    def delete_last(self):
        pass

    def delete_node(self, node):
        pass
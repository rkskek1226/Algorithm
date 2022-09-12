from collections import deque

# 이진 탐색, O(lgN)
def binary_search(l, target):
    start = 0
    end = len(l) - 1

    while start < end:
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        elif l[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


class TreeNode:
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None
        self.__parent = None

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traversal(self, cur):
        if not cur:
            return

        print(cur.key, end=" ")
        self.preorder_traversal(cur.left)
        self.preorder_traversal(cur.right)

    def inorder_traversal(self, cur):
        if not cur:
            return

        self.inorder_traversal(cur.left)
        print(cur.key, end=" ")
        self.inorder_traversal(cur.right)

    def postorder_traversal(self, cur):
        if not cur:
            return

        self.postorder_traversal(cur.left)
        self.postorder_traversal(cur.right)
        print(cur.key, end=" ")

    def levelorder_traversal(self, cur):
        q = deque()
        q.append(cur)

        while q:
            cur = q.popleft()
            print(cur.key, end=" ")

            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)

    def make_left(self, cur, left):
        cur.left = left
        if left:
            left.parent = cur

    def make_right(self, cur, right):
        cur.right = right
        if right:
            right.parent = cur

    def insert(self, key):
        new_node = TreeNode(key)

        cur = self.root
        if not cur:
            self.root = new_node
            return

        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                if not cur:
                    self.make_left(parent, new_node)
                    return
            else:
                cur = cur.right
                if not cur:
                    self.make_right(parent, new_node)
                    return

    def search(self, target):
        cur = self.root
        while cur:
            if cur.key == target:
                return cur
            elif cur.key < target:
                cur = cur.left
            else:
                cur = cur.right

    def bst_max(self, cur):   # 오른쪽으로 계속 내려가면 가장 큰 값을 찾을 수 있음
        while cur.right is not None:
            cur = cur.right
        return cur

    def bst_min(self, cur):   # 왼쪽으로 계속 내려가면 가장 작은 값을 찾을 수 있음
        while cur.left is not None:
            cur = cur.left
        return cur

    def __delete1(self, cur, target):
        if not cur:
            return None
        elif cur.key < target:
            new = self.__delete1(cur.right, target)
            self.make_right(cur, new)
        elif cur.key > target:
            new = self.__delete1(cur.left, target)
            self.make_left(cur, new)
        else:
            if not cur.left and not cur.right:   # 삭제하려는 노드가 리프 노드인 경우
                cur = None
            elif not cur.left:   # 삭제하려는 노드가 오른쪽 자식이 있을 경우
                cur = cur.right
            elif not cur.right:   # 삭제하려는 노드가 왼쪽 자식이 있을 경우
                cur = cur.left
            else:   # 삭제하려는 노드가 자식이 둘다 있을 경우
                replace = cur.left
                replace = self.bst_max(replace)
                cur.key, replace.key = replace.key, cur.key
                new = self.__delete1(cur.left, replace.key)
                self.make_left(cur, new)
        return cur

    def delete1(self, target):
        self.root = self.__delete1(self.root, target)


if __name__ == "__main__":
    bst = BST()
    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    bst.preorder_traversal(bst.get_root())
    print()
    bst.inorder_traversal(bst.get_root())
    print()
    bst.postorder_traversal(bst.get_root())
    print()
    bst.levelorder_traversal(bst.get_root())
    print()
    bst.delete1(6)
    bst.levelorder_traversal(bst.get_root())
    print()









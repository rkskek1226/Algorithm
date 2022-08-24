from Stack import Stack  # 순회를 구현하기 위함


class TreeNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None
        
    def __del(self):
        print("data {} is deleted".format(self.data))
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
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


def preorder1(cur):
    if not cur:
        return

    print(cur.data, end=" ")
    preorder1(cur.left)
    preorder1(cur.right)


def preorder2(cur):
    s = Stack()
    while True:
        while cur:
            print(cur.data, end=" ")
            s.push(cur)
            cur = cur.left

        cur = s.pop()
        if not cur:
            break

        cur = cur.right


def inorder1(cur):
    if not cur:
        return

    inorder1(cur.left)
    print(cur.data, end=" ")
    inorder1(cur.right)


def inorder2(cur):
    s = Stack()
    while True:
        while cur:
            s.push(cur)
            cur = cur.left
        cur = s.pop()

        if not cur:
            break

        print(cur.data, end=" ")
        cur = cur.right


def postorder1(cur):
    if not cur:
        return

    postorder1(cur.left)
    postorder1(cur.right)
    print(cur.data, end=" ")


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    preorder1(n1)
    print()
    preorder2(n1)
    print()
    inorder1(n1)
    print()
    inorder2(n1)
    print()
    postorder1(n1)
    print()




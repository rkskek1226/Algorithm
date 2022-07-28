class Stack:
    def __init__(self):
        self.stack = list()
        # self.top = 0

    def is_empty(self):
        if not self.stack:
            return True
        else:
            return False

    def push(self, data):
        self.stack.append(data)
        # self.top += 1

    def pop(self):
        if self.is_empty():
            return False
        else:
            # self.top -= 1
            return self.stack.pop()

    def peek(self):   # top을 조회만하고 삭제는 안함
        if self.is_empty():
            return False
        else:
            # return self.stack[self.top]
            return self.stack[-1]

    def show(self):
        for i in self.stack:
            print(i, end=" ")
        print()


s = Stack()
s.push(1)
s.show()
s.push(2)
s.show()
s.push(3)
s.show()
s.push(4)
s.show()
s.push(5)
s.show()
print("peek : {}".format(s.peek()))
print("pop : {}".format(s.pop()))
s.show()

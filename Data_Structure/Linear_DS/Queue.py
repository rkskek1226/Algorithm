# 리스트로 큐를 구현
class Queue:
    def __init__(self):
        self.queue = list()
        # self.front = 0
        # self.rear = 0

    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False

        # if self.front == self.rear:
        #     return True
        # else:
        #     return False

    def enqueue(self, data):
        self.queue.append(data)
        # self.rear += 1

    def dequeue(self):
        if self.is_empty():
            return False
        else:
            # self.front += 1
            # return self.queue.pop(self.front - 1)
            return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def show(self):
        for i in self.queue:
            print(i, end=" ")
        print()


# q = Queue()
# q.enqueue(1)
# q.show()
# q.enqueue(2)
# q.show()
# q.enqueue(3)
# q.show()
# print("peek : {}".format(q.peek()))
# print("dequeue : {}".format(q.dequeue()))
# q.show()


# collections 모듈의 dequeue 클래스로 구현
from collections import deque

queue = deque()
queue.append(0)
queue.append(1)
queue.append(2)
print(queue)
print(queue.popleft())
print(queue)


# queue 모듈의 Queue 클래스로 구현
from queue import Queue

queue = Queue()
queue.put(0)
queue.put(1)
queue.put(2)
print(queue)
print(queue.get())
print(queue)


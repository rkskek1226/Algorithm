class CircularQueue:
    MAX_SIZE = 6

    def __init__(self):
        self.list = [None for _ in range(CircularQueue.MAX_SIZE)]
        self.front = 0
        self.rear = 0   # 맨 마지막 데이터의 다음을 가리킴

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        tmp = self.rear
        tmp += 1
        if tmp >= CircularQueue.MAX_SIZE:
            tmp = 0
        if tmp == self.front:
            return True
        else:
            return False

    def enqueue(self, x):
        if not self.is_full():
            self.list[self.rear] = x
            self.rear += 1
            if self.rear >= CircularQueue.MAX_SIZE:
                self.rear = 0

    def dequeue(self):
        if not self.is_empty():
            tmp = self.list[self.front]
            self.front += 1
            if self.front >= CircularQueue.MAX_SIZE:
                self.front = 0
            return tmp

    def show(self):
        i = self.front
        while i is not self.rear:
            print("{}".format(self.list[i]), end=" ")
            i += 1
            if i >= CircularQueue.MAX_SIZE:
                i = 0
        print()


cq = CircularQueue()
cq.enqueue(0)
cq.show()
cq.enqueue(1)
cq.show()
cq.enqueue(2)
cq.show()
cq.enqueue(3)
cq.show()
cq.enqueue(4)
cq.show()
cq.dequeue()
cq.show()
cq.enqueue(5)
cq.show()







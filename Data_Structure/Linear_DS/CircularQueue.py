class Circular_Queue:
    MAX_SIZE = 10

    def __init__(self):
        self.cqueue = [None for _ in range(Circular_Queue.MAX_SIZE)]
        self.front = 0   # 가장 앞에있는 데이터의 전을 가리킴
        self.rear = 0   

    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def is_full(self):
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.is_full():
            return False
        else:
            self.rear = (self.rear + 1) % self.MAX_SIZE
            self.cqueue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            return False
        else:
            self.front = (self.front + 1) % self.MAX_SIZE
            return self.cqueue[self.front]

    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.cqueue[self.front]

    def show(self):
        i = self.front
        while i is not self.rear:
            i = (i + 1) % self.MAX_SIZE
            print(self.cqueue[i], end=" ")
        print("     front : {}, rear : {}".format(self.front, self.rear))


cq = Circular_Queue()
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
cq.enqueue(5)
cq.show()
cq.enqueue(6)
cq.show()
cq.enqueue(7)
cq.show()
cq.dequeue()
cq.show()
cq.dequeue()
cq.show()
cq.enqueue(8)
cq.show()
cq.enqueue(9)
cq.show()
cq.enqueue(10)
cq.show()


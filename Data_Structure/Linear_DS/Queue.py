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


q = Queue()
q.enqueue(1)
q.show()
q.enqueue(2)
q.show()
q.enqueue(3)
q.show()
q.enqueue(4)
q.show()
q.enqueue(5)
q.show()
print("peek : {}".format(q.peek()))
print("dequeue : {}".format(q.dequeue()))
q.show()


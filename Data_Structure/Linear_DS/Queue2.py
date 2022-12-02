import collections
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 큐를 이용한 스택 구현
class MyStack:
    def __init__(self):
        self.d = collections.deque()

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        return self.d.pop()

    def top(self) -> int:
        return self.d[-1]

    def empty(self) -> bool:
        return len(self.d) == 0


# 스택을 이용한 큐 구현
class MyQueue:
    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        return self.l.pop(0)

    def peek(self) -> int:
        return self.l[0]

    def empty(self) -> bool:
        return len(self.l) == 0


# 원형 큐 디자인
class MyCircularQueue:
    def __init__(self, k: int):
        self.l = [None] * k
        self.front = 0
        self.rear = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.l[self.rear] is None:
            self.l[self.rear] = value
            self.rear = (self.rear + 1) % self.k
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.l[self.front] is None:
            return False
        else:
            self.l[self.front] = None
            self.front = (self.front + 1) % self.k
            return True

    def Front(self) -> int:
        if self.l[self.front] is None:
            return -1
        else:
            return self.l[self.front]

    def Rear(self) -> int:
        if self.l[self.rear - 1] is None:
            return -1
        else:
            return self.l[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.l[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.l[self.front] is not None


# k개 정렬 리스트 병합
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    answer = []
    head = cur = ListNode()

    for i in lists:
        while i:
            answer.append(i.val)
            i = i.next

    answer.sort()
    for i in answer:
        tmp = ListNode(i)
        cur.next = tmp
        cur = cur.next
    return head.next


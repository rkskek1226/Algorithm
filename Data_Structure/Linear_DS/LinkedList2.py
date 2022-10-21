import collections
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 팰린드롬 연결 리스트
# 1. 리스트 변환
def isPalindrome(head: Optional[ListNode]) -> bool:
    l = []

    while head is not None:
        l.append(head.val)
        head = head.next

    while len(l) > 1:
        if l.pop(0) != l.pop():
            return False

    return True


# 2. 데크로 해결
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    q: Deque = collections.deque()

    while head is not None:
        q.append(head.val)
        head = head.next

    while len(q) > 1:
        if q.pop() != q.popleft():
            return False

    return True


# 3. 런너(Runner) 기법
def test(self, head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:   # 데이터 개수가 홀수개이면 slow 런너를 한 칸 이동시켜 중앙을 벗어나야함
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev




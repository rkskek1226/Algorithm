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
def isPalindrome(self, head: Optional[ListNode]) -> bool:
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



# 두 정렬 리스트의 병합
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = cursor = ListNode()

    while list1 or list2:
        if list1 and list2:
            if list1.val <= list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
        elif list1:
            cursor.next = list1
            list1 = list1.next
        else:
            cursor.next = list2
            list2 = list2.next

    return head.next



# 역순 연결 리스트
# 반복 구조로 뒤집기
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None

    while head:
        cursor, head = head, head.next
        cursor.next, prev = prev, cursor

    return prev



# 두 수의 덧셈
# 1. 혼자 푼 방식
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    prev1, prev2, prev3 = None, None, None
    head = node = ListNode()

    while l1:
        cursor, l1 = l1, l1.next
        prev1, cursor.next = cursor, prev1

    while l2:
        cursor, l2 = l2, l2.next
        prev2, cursor.next = cursor, prev2

    tmp1, tmp2 = "", ""

    while prev1:
        tmp1 += str(prev1.val)
        prev1 = prev1.next

    while prev2:
        tmp2 += str(prev2.val)
        prev2 = prev2.next

    tmp3 = str(int(tmp1) + int(tmp2))

    # for i in tmp3:
    #     node.next = ListNode(val=int(i))
    #     node = node.next
    #
    # head = head.next
    #
    # while head:
    #     cursor, head = head, head.next
    #     prev3, cursor.next = cursor, prev3

    for i in tmp3:
        n = ListNode(val=int(i))
        n.next = prev3
        prev3 = n

    return prev3


# 2. 전가산기 방식으로 구현
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = cursor = ListNode()

    carry = 0

    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        cursor.next = ListNode(val=val)
        cursor = cursor.next

    return head.next



# 페어의 노드 스왑
# 1. 단순히 값만 교환
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head



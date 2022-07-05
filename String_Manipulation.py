import collections
import heapq
import functools
import itertools
import re,sys, math, bisect
from typing import *

# 문자열 작업은 슬라이싱으로 처리하는 것이 빠름
# s1 = "12345"   s2 = s1[::-1] -> s1 문자열 뒤집은 것을 저장
# s1 = ["1, 2, 3]   s2 = s1[::-1] -> s1 원소들을 뒤집은 것을 저장
# 플랫폼마다 s1 = s2[::-1]이 되는 곳이 있고 안되는 곳이 있는데 안되는 곳에서는 s1[:] = s2[::-1]로 할 것

# 팰린드롬(Palindrome)(뒤집어도 같은 말이 되는 단어나 문장)
# 1. 리스트로 푸는 방법
def is_palindrome(self, s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


# 2. 데크로 푸는 방법
def is_palindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():   # 리스트의 pop(0)은 O(n)이지만 데크의 popleft()는 O(1)
            return False

    return True





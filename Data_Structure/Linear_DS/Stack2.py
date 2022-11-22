import collections
from typing import *


# 중복 문자 제거
# 1. 스택 일치 여부 판별
def isValid(self, s: str) -> bool:
    l = []
    dic = {")": "(", "}": "{", "]": "["}

    for i in s:
        if i not in dic.keys():
            l.append(i)
        else:
            if not l or l.pop() != dic[i]:
                return False

    return len(l) == 0








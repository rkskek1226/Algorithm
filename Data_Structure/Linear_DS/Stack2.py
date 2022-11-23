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



# 일일 온도
# 1. 스택 값 비교
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    s = []

    for i, cur in enumerate(temperatures):
        while s and cur > temperatures[s[-1]]:
            last = s.pop()
            answer[last] = i - last

        s.append(i)

    return answer








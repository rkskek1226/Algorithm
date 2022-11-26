import collections
import heapq
from typing import *


# 해시맵 디자인
class MyHashMap:
    def __init__(self):
        self.dict = {}

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value

    def get(self, key: int) -> int:
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.dict.keys():
            del self.dict[key]


# 보석과 돌
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    c = collections.Counter(stones)
    answer = 0

    for i in jewels:
        answer += c[i]

    return answer


# 중복문자 없는 가장 긴 부분 문자열
# 1. 슬라이딩 윈도우와 투 포인터로 사이즈 조절


# 상위 k번 빈도 요소
# 1. 파이썬다운 방식
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    c = collections.Counter(nums)
    answer = []

    tmp = c.most_common(k)
    for i in tmp:
        answer.append(i[0])

    return answer


# Counter를 이용한 음수 순 추출
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    c = collections.Counter(nums)
    tmp = []
    answer = []

    for i in c:
        heapq.heappush(tmp, (-c[i], i))

    for i in range(k):
        answer.append(heapq.heappop(tmp)[1])

    return answer



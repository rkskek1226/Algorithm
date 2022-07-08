# 메모리 공간 기반의 연속 방식
# 값의 집합으로 구성된 구조로 인덱스로 식별함
# 데이터 조회 시 O(1)
# 자동으로 크기를 조절하는 배열인 동적 배열이 파이썬에서는 리스트

from typing import *

# 두 수의 합
# 1. 브루트 포스(무차별 대입 방식)
def twoSum(nums: List[int], target: int) -> List[int]:
    for a in range(len(nums) - 1):
        for b in range(a + 1, len(nums)):
            if nums[a] + nums[b] == target:
                return [a, b]


# 2. in 연산자 이용(브루트 포스보다 빠름)
def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        tmp = target - n

        if tmp in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(tmp) + (i + 1)]





















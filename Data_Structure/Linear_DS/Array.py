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



# 세 수의 합
# 1. 브루트 포스( O(n^3), 시간 제한 걸림 )
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for a in range(len(nums) - 2):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        for b in range(a + 1, len(nums) - 1):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue
            for c in range(b + 1, len(nums)):
                if c > b + 1 and nums[c] == nums[c - 1]:
                    continue
                if nums[a] + nums[b] + nums[c] == 0:
                    result.append([nums[a], nums[b], nums[c]])

    return result


# 2. 투 포인터( O(n^2), 시간 제한 안걸림 )
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            else:
                left += 1

    return result



# 배열 파티션 1
# 1. 오름차순 풀이
def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    sum = 0

    for i in range(0, len(nums), 2):
        sum += min(nums[i], nums[i + 1])

    return sum


# 2. 파이썬다운 풀이
def arrayPairsum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])



















import collections
import itertools
from typing import *


# 섬의 갯수
# 1. DFS로 그래프 탐색
def dfs(self, grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
        return

    grid[i][j] = "0"
    self.dfs(grid, i, j + 1)
    self.dfs(grid, i, j - 1)
    self.dfs(grid, i + 1, j)
    self.dfs(grid, i - 1, j)


def numIslands(self, grid: List[List[str]]) -> int:
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                self.dfs(grid, i, j)
                count += 1

    return count


# 전화번호 문자 조합
# 1. 모든 조합 탐색
def letterCombinations(self, digits: str) -> List[str]:
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    if not digits:
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    dfs(0, "")

    return result


# 2. itertools 모듈 사용
def letterCombinations(self, digits: str) -> List[str]:
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    tmp = []

    if not digits:
        return []

    for i in digits:
        tmp.append(dic[i])

    p = list(itertools.product(*tmp))

    for i in range(len(p)):
        p[i] = "".join(p[i])

    return p


# 순열
# 1. itertools 모듈 사용
def permute(self, nums: List[int]) -> List[List[int]]:
    p = itertools.permutations(nums)
    return list(p)


# 조합
# 1. itertools 모듈 사용
def combine(self, n: int, k: int) -> List[List[int]]:
    tmp = "1"
    for i in range(2, n + 1):
        tmp += str(i)

    c = list(itertools.combinations(tmp, k))

    for i in range(len(c)):
        c[i] = [int(j) for j in c[i]]

    return c


# 조합의 합
# 1. ㅁㄴㅇ



# 2. itertools 모듈 사용(시간 초과)
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    answer = []
    candidates.sort()

    if candidates[0] > target:
        return []

    m = int(target / candidates[0])

    for i in range(1, m + 1):
        c = itertools.combinations_with_replacement(candidates, i)
        for j in c:
            if j[0] > target:
                continue
            if sum(j) == target:
                answer.append(list(j))

    return answer


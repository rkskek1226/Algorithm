import sys
import itertools

L, C = map(int, sys.stdin.readline().rstrip().split())
arr = list(sys.stdin.readline().rstrip().split())
arr.sort()
vowels = ["a", "e", "i", "o", "u"]

all_case = list(itertools.combinations(arr, L))

for case in all_case:
    cnt = 0
    for i in case:
        if i in vowels:
            cnt += 1

    if cnt >= 1 and L - cnt >= 2:
        print("".join(case))

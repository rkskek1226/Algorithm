import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))
test_n = int(sys.stdin.readline().strip())
test_case = list(map(int, sys.stdin.readline().split()))


counter = Counter(l)

for i in test_case:
    print(counter[i], end=" ")


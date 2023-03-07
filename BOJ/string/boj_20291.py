import collections

n = int(input())
d = collections.defaultdict(int)

for _ in range(n):
    _, tmp = input().split(".")
    d[tmp] += 1

d = sorted(d.items())

for i in d:
    print(i[0], i[1])


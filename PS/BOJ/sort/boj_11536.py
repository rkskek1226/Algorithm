import sys


def func(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    return result


n = int(sys.stdin.readline().strip())
l = []

for _ in range(n):
    l.append(sys.stdin.readline().strip())

l.sort(key=lambda x: (len(x), func(x), x))
for i in l:
    print(i)

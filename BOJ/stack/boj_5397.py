import sys

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    left, right = [], []

    for i in s:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)

    # left.extend(reversed(right))
    left.extend(sorted(right, reverse=True))
    print("".join(left))



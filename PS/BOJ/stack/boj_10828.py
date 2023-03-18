import sys

n = int(sys.stdin.readline())
s = []

for _ in range(n):
    tmp = sys.stdin.readline().split()

    if tmp[0] == "push":
        s.append(int(tmp[1]))

    elif tmp[0] == "top":
        if not s:
            print("-1")
        else:
            print(s[-1])

    elif tmp[0] == "pop":
        if not s:
            print("-1")
        else:
            print(s.pop())

    elif tmp[0] == "size":
        print(len(s))

    elif tmp[0] == "empty":
        if not s:
            print("1")
        else:
            print("0")


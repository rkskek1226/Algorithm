import sys

tmp = sys.stdin.readline().strip()

stack = []

for i in tmp:
    if i == "(":
        stack.append(i)
    else:
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(i)

print(len(stack))

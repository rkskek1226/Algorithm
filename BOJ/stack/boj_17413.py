import sys

s = sys.stdin.readline().rstrip()
s += " "
result = ""
stack = []
tag_flag = False

for i in s:
    if i == "<":
        tag_flag = True
        while stack:
            result += stack.pop()
        result += "<"
    elif i == ">":
        tag_flag = False
        result += ">"
    else:
        if tag_flag:
            result += i
        else:
            if i != " ":
                stack.append(i)
            else:
                while stack:
                    result += stack.pop()
                result += " "

print(result)
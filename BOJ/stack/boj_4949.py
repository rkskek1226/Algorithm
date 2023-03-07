s_list = []
d = {")": "(", "]": "["}

while True:
    try:
        s_list.append(input())
    except:
        break

for s in s_list:
    result = "yes"
    stack = []

    if s[0] == ".":
        break

    if s[-1] != ".":
        print("no")
        continue

    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) == 0 or stack.pop() != d[i]:
                result = "no"
                break

    if len(stack) != 0:
        result = "no"
    print(result)

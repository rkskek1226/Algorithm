
import sys

s = sys.stdin.readline().rstrip()
num_list = []
op_list = []

tmp = ""
for i in s:
    if i.isdigit():
        tmp += i
    else:
        num_list.append(int(tmp))
        op_list.append(i)
        tmp = ""

num_list.append(int(tmp))

for i in range(len(op_list) - 1):
    if op_list[i] == "-" and op_list[i + 1] == "+":
        op_list[i + 1] = "-"

result = num_list.pop(0)
for i in range(len(op_list)):
    if op_list[i] == "+":
        result += num_list[i]
    else:
        result -= num_list[i]

print(result)

import sys

n = int(sys.stdin.readline())

length_list = list(map(int, sys.stdin.readline().split()))
price_list = list(map(int, sys.stdin.readline().split()))
price_list.pop()
result = 0

for i in range(len(price_list)):
    if price_list[i] <= min(price_list[i:]):
        result += price_list[i] * sum(length_list[i:])
        break
    else:
        result += price_list[i] * length_list[i]

print(result)

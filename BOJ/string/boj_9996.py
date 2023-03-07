n = int(input())
pattern = str(input())
result = []

for _ in range(n):
    tmp = input()
    if tmp[0] == pattern[0] and tmp[-1] == pattern[-1]:
        result.append("DA")
    else:
        result.append("NE")

for i in result:
    print(i)
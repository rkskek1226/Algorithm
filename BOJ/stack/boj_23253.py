n, m = map(int, input().split())
result = "Yes"

for i in range(m):
    tmp = input()
    data = list(map(int, input().split()))

    if data != sorted(data, reverse=True):
        result = "No"
        break

print(result)

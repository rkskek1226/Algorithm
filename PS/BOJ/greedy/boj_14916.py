import sys

money = int(sys.stdin.readline())
cnt = 0

while money != 0:
    if money % 5 == 0:
        cnt += (money // 5)
        break
    else:
        money -= 2
        cnt += 1

    if money <= 1:
        cnt = -1
        break

print(cnt)

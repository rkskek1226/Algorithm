import sys

money = 1000 - int(sys.stdin.readline())
change = [500, 100, 50, 10, 5, 1]
cnt = 0

'''
while money != 0:
    for i in change:
        tmp = money // i
        cnt += tmp
        money -= (i * tmp)

print(cnt)
'''

for i in change:
    if money == 0:
        break

    tmp = money // i
    cnt += tmp
    money %= i

print(cnt)



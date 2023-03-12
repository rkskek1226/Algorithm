import sys


def dfs_1(i, j):   # -일 경우
    global room, n, m

    if j < 0 or j >= m:
        return

    if room[i][j] == "-":
        room[i][j] = "x"

        dfs_1(i, j - 1)
        dfs_1(i, j + 1)


def dfs_2(i, j):   # |일 경우
    global room, n, m

    if i < 0 or i >= n:
        return

    if room[i][j] == "|":
        room[i][j] = "x"

        dfs_2(i - 1, j)
        dfs_2(i + 1, j)


n, m = map(int, sys.stdin.readline().rstrip().split())
room = []
cnt = 0

for i in range(n):
    tmp = sys.stdin.readline().strip()
    tmp_list = []
    for j in tmp:
        tmp_list.append(j)
    room.append(tmp_list)

for i in range(n):
    for j in range(m):
        if room[i][j] == "-":
            dfs_1(i, j)
            cnt += 1
        elif room[i][j] == "|":
            dfs_2(i, j)
            cnt += 1


print(cnt)


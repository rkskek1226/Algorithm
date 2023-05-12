import sys


# 상하좌우
def ps1_1():
    N = int(sys.stdin.readline().rstrip())
    order = list(sys.stdin.readline().rstrip().split())

    x, y = 0, 0

    for i in order:
        if i == "L":
            if y > 0:
                y -= 1
        elif i == "R":
            if y < N - 1:
                y += 1
        elif i == "U":
            if x > 0:
                x -= 1
        elif i == "D":
            if x < N - 1:
                x += 1

    print(x + 1, y + 1)


def ps1_2():
    N = int(sys.stdin.readline().rstrip())
    order = list(sys.stdin.readline().rstrip().split())

    x, y = 1, 1

    move_type = ["L", "R", "U", "D"]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in order:
        for move in range(len(move_type)):
            if move_type[move] == i:
                new_x = x + dx[move]
                new_y = y + dy[move]

        if new_x < 1 or new_x > N or new_y < 1 or new_y > N:
            continue
        else:
            x = new_x
            y = new_y


    print(x, y)


# 시각
def ps2_1():
    N = int(sys.stdin.readline().rstrip())
    h, m, s = 0, 0, 0
    answer = 0

    while h < N + 1:
        if s == 60:
            m += 1
            s = 0

        if m == 60:
            h += 1
            m = 0

        s += 1

        if "3" in str(h) or "3" in str(m) or "3" in str(s):
            answer += 1

    print(answer)


def ps2_2():
    N = int(sys.stdin.readline().rstrip())
    answer = 0

    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) or "3" in str(j) or "3" in str(k):
                    answer += 1

    print(answer)


# 왕실의 나이트
def ps3():
    start = sys.stdin.readline().rstrip()
    x, y = int(start[1]), start[0]
    y = ord(y) - 96
    answer = 0

    move_ranges = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    for move_range in move_ranges:
        new_x = move_range[0] + x
        new_y = move_range[1] + y

        if new_x >= 1 and new_x <= 8 and new_y >= 1 and new_y <= 8:
            answer += 1

    print(answer)


# 게임 개발
def ps4():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    x, y, tmp_face = map(int, sys.stdin.readline().rstrip().split())
    faces = []
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]   # "north", "west", "south", "east"
    answer = 0
    turn_time = 0
    
    game_map = []
    for _ in range(N):
        game_map.append(list(map(int, sys.stdin.readline().rstrip().split())))
    game_map[x][y] = -1

    while True:
        tmp_face += 1
        tmp_face %= len(moves)

        
        new_x = x + moves[tmp_face][0]
        new_y = y + moves[tmp_face][1]

        if game_map[new_x][new_y] == 0:
            x, y = new_x, new_y
            answer += 1
            turn_time = 0
            game_map[new_x][new_y] = -1
        else:
            turn_time += 1

        if turn_time == 4:
            if game_map[x + moves[(tmp_face + 2) % len(moves)][0]][y + moves[(tmp_face + 2) % len(moves)][1]] != 1:
                x = x + moves[(tmp_face + 2) % len(moves)][0]
                y = y + moves[(tmp_face + 2) % len(moves)][1]
            else:
                break

    print(answer)


ps4()


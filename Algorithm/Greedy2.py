import sys


# 큰 수의 법칙
def ps2():
    N, M, K = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort(reverse=True)
    cnt = 0
    answer = 0

    for _ in range(M):
        if cnt == K:
            answer += arr[1]
            cnt = 0
        else:
            answer += arr[0]
            cnt += 1

    print(answer)


# 1이 될 때까지
def ps4():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0

    while N != 1:
        if N % K == 0:
            N /= K
        else:
            N -= 1
        cnt += 1

    print(cnt)


# 모험가 길드
def q1():
    pass

ps4()
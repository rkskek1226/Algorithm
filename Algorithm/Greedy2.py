import sys
import itertools
import collections


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
    N = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort()
    answer = 0
    cnt = 0

    for i in arr:
        cnt += 1

        if cnt >= i:
            answer += 1
            cnt = 0

    print(answer)    


# 곱하기 혹은 더하기
def q2():
    s = sys.stdin.readline().rstrip()
    answer = int(s[0])

    for i in range(1, len(s)):
        if int(s[i]) <= 1 or answer <= 1:
            answer += int(s[i])
        else:
            answer *= int(s[i])

    print(answer)


# 문자열 뒤집기
def q3():
    s = sys.stdin.readline().rstrip()

    cnt_0 = 0
    cnt_1 = 0

    flag_0 = False
    flag_1 = False
    for i in range(len(s)):
        if s[i] == "0":
            if not flag_0:
                cnt_0 += 1
                flag_0 = True

            flag_1 = False
            
        else:
            flag_0 = False

            if not flag_1:
                cnt_1 += 1
                flag_1 = True
        
    print(min(cnt_0, cnt_1))


# 만들 수 없는 금액
def q4():
   pass


# 볼링공 고르기
def q5_1():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    arr.sort()
    answer = 0

    for i in range(len(arr) - 1):
        if arr[i] in arr[i + 1:]:
            cnt = arr[i + 1:].count(arr[i])
            answer += (len(arr) - i - 1 - cnt)
        else:
            answer += (len(arr) - i - 1)

    print(answer)


def q5_2():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    counter = collections.Counter(arr)
    answer = 0

    for k in counter.keys():
        N -= counter[k]
        answer += (counter[k] * N)

    print(answer)


q5_2()
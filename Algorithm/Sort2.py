import sys
import heapq


# 국영수
def q1():
    N = int(sys.stdin.readline().rstrip())
    arr = []

    for _ in range(N):
        tmp = list(sys.stdin.readline().rstrip().split())
        arr.append((tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])))

    arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for i in arr:
        print(i[0])


# 실패율
def q3(N, stages):
    answer = []
    arr = []
    
    for i in range(N):
        tmp = 0
        for stage in stages:
            if stage >= (i + 1):
                tmp += 1
                
        if tmp == 0:
            arr.append((i + 1, 0))
        else:
            arr.append((i + 1, stages.count(i + 1) / tmp))
            
    arr.sort(key=lambda x: (-x[1], x[0]))
    for i in arr:
        answer.append(i[0])
    
    return answer


# 카드 정렬하기
def q4():
    N = int(sys.stdin.readline().rstrip())
    arr = []
    tmp = []
    answer = 0

    for _ in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))

    heapq.heapify(arr)

    while arr:
        tmp.append(heapq.heappop(arr))

        if len(tmp) == 2:
            heapq.heappush(arr, sum(tmp))
            answer += sum(tmp)
            tmp = []
            
    print(answer)


q1()
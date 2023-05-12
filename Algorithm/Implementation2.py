import sys


# 럭키 스트레이트
def q1():
    N = list(map(int, sys.stdin.readline().rstrip()))

    left = N[:len(N) // 2]
    right = N[len(N) // 2:]

    if sum(left) == sum(right):
        print("LUCKY")
    else:
        print("READY")


# 문자열 재정렬
def q2():
    s = sys.stdin.readline().rstrip()

    digit = []
    non_digit = []

    for i in s:
        if i.isdigit():
            digit.append(int(i))
        else:
            non_digit.append(i)

    non_digit.sort()
    non_digit = "".join(non_digit)
    print(non_digit + str(sum(digit)))


# 문자열 압축
def q3(s):
    answer = 0
    result = []
    
    for i in range(1, len(s)):
        tmp = ""
        prev = s[:i]
        cnt = 0
        left = 0
        right = i
        
        while left < len(s):
            if s[left:left + i] == prev:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += prev
                else:
                    tmp += (str(cnt) + prev)
                    cnt = 1
                prev = s[left:left + i]
            left += i
            
        if cnt == 1:
            tmp += prev
        else:
            tmp += (str(cnt) + prev)
        
        result.append(len(tmp))
        
    answer = min(result)
    return answer

q2()
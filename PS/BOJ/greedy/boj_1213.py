import sys
import collections

s = sys.stdin.readline().rstrip()
counter = collections.Counter(s)
center = ""
cnt = 0
answer = ""

for k, v in counter.items():
    if v % 2 != 0:
        cnt += 1
        center = k

if cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    counter = dict(sorted(counter.items(), key=lambda x: x[0]))

    for k, v in counter.items():
        answer += k * (v // 2)
    
    answer = answer + center + answer[::-1]
    print(answer)

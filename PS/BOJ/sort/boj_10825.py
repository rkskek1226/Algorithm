import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(n):
    tmp = sys.stdin.readline().rstrip().split()
    name = tmp[0]
    kor = int(tmp[1])
    eng = int(tmp[2])
    mat = int(tmp[3])
    arr.append((name, kor, eng, mat))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])


# 못 품
import sys
import collections


N = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0

weights.sort(reverse=True)
boxes = collections.deque(sorted(boxes, reverse=True))
k = 1

if weights[0] < boxes[0]:
    answer = -1
else:
    while boxes:
        for weight in weights:
            if boxes:
                for box in boxes:
                    if weight >= box:
                        boxes.popleft()
                        break

        answer += 1

print(answer)

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
heap = list(map(int, sys.stdin.readline().rstrip().split()))
heapq.heapify(heap)

for _ in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    heapq.heappush(heap, (a + b))
    heapq.heappush(heap, (a + b))

print(sum(heap))

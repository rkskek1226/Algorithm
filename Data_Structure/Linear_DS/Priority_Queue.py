import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap, "\n")

print(heapq.heappop(heap))
print(heap, "\n")

heap = [4, 1, 7, 3, 8, 5]
print(heap, " -> ", end=" ")
heapq.heapify(heap)
print(heap, "\n")


# heapq 모듈은 최소 힙(mean heap)으로 동작
# 최대 힙으로 활용하려면 별도의 방법이 필요
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))
print(heap)

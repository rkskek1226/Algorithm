# 알고리즘
# 1. 출발 노드와 도착 노드를 설정하고 최단 거리 테이블을 초기화
# 2. 현재 위치한 노드와 인접한 노드 중 방문하지 않은 노드들 중 거리가 가장 짧은 노드를 선택
# 3. 해당 노드를 방문 처리하고 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블을 업데이트
# 4. 2~3 과정을 반복


import heapq
from collections import defaultdict
from typing import *


# 네트워크 딜레이 타임
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    dist = defaultdict(int)

    for u, v, w in times:
        graph[u].append((v, w))

    q = [(0, k)]  # (소요시간, 정점) 구조

    while q:
        time, node = heapq.heappop(q)

        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(q, (time + w, v))

    if len(dist) == n:
        return max(dist.values())
    else:
        return -1



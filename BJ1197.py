import heapq
from collections import deque
import sys
input = sys.stdin.readline

V, E = map(int,input().split())

# MST
# 간선을 인접리스트에 집어넣기
# 힙에 시작점 넣기
# 힙이 빌때까지
# 힙의 최소값 꺼내서 방문 확인
# 방문 안했으면
# 방문 표시, 비용 추가, 간선들 힙에 넣기

edge = [[] for _ in range(V+1)]
visited = [False] * (V+1)
result = 0
for i in range(E) :
    A,B,C = map(int,input().split())
    # A : vertex, B : vertex, C : edge
    edge[A].append([C,B])
    edge[B].append([C,A])
# [비중치,VERTEX]
heap = [[0,1]]

while heap :
    w, each_node = heapq.heappop(heap)
    if not visited[each_node] :
        visited[each_node] = True
        result += w
        for v in edge[each_node] :
            if not visited[v[1]] :
                heapq.heappush(heap, v)

print(result)

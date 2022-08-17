import heapq
from collections import deque

import sys

input = sys.stdin.readline

v, e = map(int,input().split())

k = int(input())

INF = sys.maxsize
adjlist = [[] for _ in range(v+1)]
visited = [False] * (v+1)
distance = [INF] * (v+1)

for _ in range(e) :
    u, v2, w = map(int,input().split())
    adjlist[u].append([w,v2])


heap = []

heapq.heappush(heap,[0,k])
distance[k] = 0
while heap :
    weight, node = heapq.heappop(heap)
    if distance[node] < weight :
        continue
    for edge in adjlist[node] :
        if distance[edge[1]] > weight + edge[0] :
            distance[edge[1]] = weight + edge[0]
            heapq.heappush(heap,[distance[edge[1]], edge[1]])

for i in range(1,v+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])

import heapq
from collections import deque

import sys

input = sys.stdin.readline

v, e = map(int,input().split())

adjlist = [[] for _ in range(v+1)]
visited = [False]* (v+1)
for _ in range(e) :
    a,b,c = map(int,input().split())
    adjlist[a].append((c,b))
    adjlist[b].append((c,a))

cost = 0
heap = [[0,1]]

while heap :
    weight, vertex = heapq.heappop(heap)
    if visited[vertex] == False :
        visited[vertex] = True
        cost += weight
        for edge in adjlist[vertex] :
            if visited[edge[1]] == False :
                heapq.heappush(heap,edge)

print(cost)

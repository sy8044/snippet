import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

adjlist = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cost = 0
for _ in range(m) :
    a,b,c = map(int,input().split())
    adjlist[a].append((c,b))
    adjlist[b].append((c,a))

heap = [[0,1]]

while heap :
    weight, node = heapq.heappop(heap)
    if visited[node] == False :
        cost += weight
        visited[node] = True
        for edge in adjlist[node] :
            if visited[edge[1]] == False :
                heapq.heappush(heap,edge)

print(cost)

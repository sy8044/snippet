import heapq
from collections import deque

import sys

input = sys.stdin.readline

n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque()
q.append(x)

INF = int(1e6)
dist = [INF] * (n+1)
dist[x] = 0
while q:
    now = q.popleft()
    for node in graph[now] :
        if dist[now] + 1 < dist[node] :
            dist[node] = dist[now] + 1
            q.append(node)

if k not in dist :
    print(-1)
for i in range(1,n+1) :
    if dist[i] == k :
        print(i)

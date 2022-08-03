import heapq
from collections import deque

import sys

input = sys.stdin.readline

node = int(input())

edge = int(input())

adj = [[] for _ in range(node+1)]
for _ in range(edge) :
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque()

q.append(1)
visited = [False] * (node+1)
visited[1] = True
count = 0
while q :
    n = q.popleft()
    for dest in adj[n] :
        if visited[dest] == False :
            count += 1
            q.append(dest)
            visited[dest] = True
print(count)

import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

m,n = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

q = deque()

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            q.append((i,j))

while q :
    y,x = q.popleft()
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<m :
            if graph[ny][nx] == 0 :
                q.append((ny,nx))
                graph[ny][nx] = graph[y][x] + 1
ans = 0
flag = True
for i in range(n) :
    ans = max(ans,max(graph[i]))
    if 0 in graph[i] :
        flag = False

if not flag :
    print(-1)
else :
    print(ans-1)

import heapq
from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]



count = 0
msize = 0

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def bfs(y,x) :
    q = deque()
    q.append((y,x))
    size = 1

    while q :
        cy, cx = q.popleft()
        for i in range(4) :
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and 0<=nx<m :
                if graph[ny][nx] == 1 :
                    graph[ny][nx] = 2
                    q.append((ny,nx))
                    size += 1
    return size

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            count += 1
            graph[i][j] = 2
            msize = max(msize,bfs(i,j))

print(count)
print(msize)

#bfs
import collections
import heapq
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [list(map(int,input().strip())) for _ in range(n)]
weight = [[0]*m for _ in range(n)]

y,x = 0,0

q = deque()
q.append([y,x])
dy = [0,1,0,-1]
dx = [1,0,-1,0]

while q :
    currentY, currentX = q.popleft()
    graph[currentY][currentX] = 2
    for i in range(4) :
        nextY = currentY + dy[i]
        nextX = currentX + dx[i]
        if 0<=nextY<n and 0<=nextX<m :
            if graph[nextY][nextX] == 1 :
                q.append([nextY,nextX])
                graph[nextY][nextX] = 2
                weight[nextY][nextX] = weight[currentY][currentX] + 1

print(weight[n-1][m-1]+1)

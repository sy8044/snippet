import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

r,c, n = map(int,input().split())

graph = [list(input()) for _ in range(r)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

bomb = deque()

def bfs(graph,bomb) :
    while bomb :
        row, col = bomb.popleft()
        graph[row][col] = '.'

        for d in range(4):
            nr, nc = row + dy[d], col + dx[d]
            if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] == 'O':
                graph[nr][nc] = '.'

# 1초
for i in range(r) :
    for j in range(c) :
        if graph[i][j] == 'O' :
            bomb.append((i,j))

for a in range(2,n+1) :
    # 모든 칸에 폭탄 설치
    if a % 2 == 0 :
        for i in range(r) :
            for j in range(c) :
                graph[i][j] = 'O'
    else :
        bfs(graph,bomb)
        for i in range(r) :
            for j in range(c) :
                if graph[i][j] == 'O' :
                    bomb.append((i,j))
for row in graph:
    print(''.join(row))




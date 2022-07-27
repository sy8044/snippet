import heapq
from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

r,c,d = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range (n)]



dy = [-1,0,1,0]
dx = [0,1,0,-1]

count = 0

while True :
    if graph[r][c] == 0 :
        # 1. 현재 위치를 청소한다
        graph[r][c] = 2
        count += 1
    flag = False
    for i in range(1,5) :
    # 2. 왼쪽방향부터 탐색 진행
        nr = r + dy[d-i]
        nc = c + dx[d-i]

        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
        if 0<=nr<n and 0<=nc<m :
            if graph[nr][nc] == 0 :
                # 그 방향으로 회전하고
                d = (d-i+4) % 4
                # 한 칸을 전진하고
                r = nr
                c = nc
                flag = True
                # 1번부터 진행한다
                break

    # 4 방향 모두 청소가 되어있다면
    if flag == False :

        nr = r - dy[d]
        nc = c - dx[d]
        if 0<=nr<n and 0<=nc<m :
            # 뒤쪽 방향이 벽이면 정지
            if graph[nr][nc] == 1 :
                break
            else :
            # 방향 유지하여 한칸 후진 후 2번으로 돌아감감
                r = nr
                c = nc
        else :
            break
            
print(count)

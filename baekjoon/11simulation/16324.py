import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n, l , r = map(int ,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]




def bfs(y, x) :
    global team
    union[y][x] = team
    sum = a[y][x]
    count = 1
    q = deque()
    move = deque()
    q.append((y,x))
    move.append((y,x))
    while q:
        cy,cx = q.popleft()
        for i in range(4) :
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<n and  0<=nx<n and union[ny][nx] == 0:
                temp = abs(a[cy][cx]-a[ny][nx])
                if l <= temp <= r :
                    union[ny][nx] = team
                    q.append((ny,nx))
                    move.append((ny,nx))
                    sum += a[ny][nx]
                    count += 1
    for d in move :
        a[d[0]][d[1]] = sum//count
# def movePeople(num) :
#     for i in range(n) :
#         for j in range(n) :
#             if union[i][j] == num :
#                 a[i][j] = people[num-1]

day = 0
while True :
    union = [[0] * n for _ in range(n)]
    flag = True
    # 국경선을 연다
    team = 1
    for i in range(n) :
        for j in range(n) :
            if union[i][j] == 0 :
                union[i][j] = team
                bfs(i,j)
                team += 1
                if team > (n**2) :
                    flag = False
    if not flag :
        break
    # 인구이동을 시작한다
    # for i in range(team-1) :
    #     movePeople(i+1)


    day += 1

print(day)


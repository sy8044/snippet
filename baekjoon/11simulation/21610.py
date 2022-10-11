import heapq
import itertools
from collections import deque
import collections
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
a = []

for _ in range(n) :
    a.append(list(map(int,input().split())))

dy = [0,0,-1,-1,-1,0,1,1,1]
dx = [0,-1,-1,0,1,1,1,0,-1]

clouds = [[n - 1, 0], [n - 2, 0], [n - 1, 1], [n - 2, 1]]


def bug(r,c,a) :
    dy = [-1,-1,1,1]
    dx = [-1,1,1,-1]
    for i in range(4) :
        ny = r + dy[i]
        nx = c + dx[i]
        if 0<=ny<n and 0<=nx<n :
            if a[ny][nx] > 0 :
                a[r][c] += 1


for _ in range(m) :
    newclouds = []
    d ,s = map(int,input().split())
    # 구름이 d 방향으로 s만큼 이동한다
    for cloud in clouds :
        nr = cloud[0]
        nc = cloud[1]
        nr +=(dy[d]*s)
        nc += (dx[d]*s)
        nr = nr % n
        nc = nc % n
        newclouds.append([nr,nc])
    # 각 구름에서 비가 내려 물 양이 1증가
    # 구름이 모두 사라진다
    visited = [[False]*n for _ in range(n)]
    for cloud in newclouds :
        a[cloud[0]][cloud[1]] += 1
        visited[cloud[0]][cloud[1]] = True
    clouds = []
    # 물이 증가한칸에 물복사버그 시전
    for cloud in newclouds :
        bug(cloud[0],cloud[1],a)
    # 구름 생성, 물양 -2

    for i in range(n) :
        for j in range(n) :
            if a[i][j] >= 2 :
                if visited[i][j] == False :
                    a[i][j] -= 2
                    clouds.append([i,j])
ans = 0
for r in a :
    ans += sum(r)
print(ans)

import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

graph = [list(input().strip()) for _ in range(n)]

find = [list(input().strip()) for _ in range(n)]

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]
ans = [[0] * n for _  in range(n)]
def check(y,x) :
    count = 0
    for i in range(8) :
        ny = y +dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n :
            if graph[ny][nx] == '*' :
                count += 1
    return count

flag = False
for i in range(n) :
    for j in range(n) :
        if find[i][j] == 'x' :
            if graph[i][j] == "*" :
                flag = True
            else :
                find[i][j] = check(i,j)
if flag == True :
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] == "*" :
                find[i][j] = "*"

for i in range(n) :
    for j in range(n) :
        print(find[i][j],end='')
    print()

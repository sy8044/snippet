import heapq
from collections import deque

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

adjlist = [[] for _ in range(n+1)]
ans = []
for _ in range(m) :
    a , b = map(int,input().split())
    adjlist[b].append(a)

def bfs(i) :
    visited = [False] * (n+1)
    q = deque()
    temp = 1
    q.append(i)
    visited[i] = True
    while q :
        now = q.popleft()
        for com in adjlist[now] :
            if visited[com] == False :
                q.append(com)
                temp += 1
                visited[com] = True
    return temp

maxcount = 0
for j in range(n+1) :
    temp = bfs(j)
    if temp > maxcount :
        maxcount = temp
        ans.clear()
        ans.append(j)
    elif temp == maxcount :
        ans.append(j)

print(*ans)

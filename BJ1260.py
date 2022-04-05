# dfs, bfs
import collections
import heapq
from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

ll = [[] for _ in range(n+1)]

for i in range(m) :
    a , b = map(int,input().split())
    ll[a].append(b)
    ll[b].append(a)

for i in range(n+1) :
    ll[i].sort()
visited = [False] * (n+1)
def dfs(v) :
    visited[v] = True
    print(v, end = " ")
    for node in ll[v] :
        if not visited[node] :
            dfs(node)

def bfs(v) :
    q = deque()
    visited[v] = True
    q.append(v)
    print(v, end = " ")
    while q :
        nodelist = q.popleft()
        for node in ll[nodelist] :
            if not visited[node] :
                q.append(node)
                visited[node] = True
                print(node, end = " ")

dfs(v)
print()
visited = [False] * (n+1)


bfs(v)

import heapq
from collections import deque

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

adjlist = [[] for _ in range(n+1)]
parent = [-1] * (n+1)
for _ in range(n-1) :
    a,b = map(int,input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
parent[1] = 0
def dfs(n) :
    for node in adjlist[n] :
        if parent[node] == -1 :
            parent[node] = n
            dfs(node)

dfs(1)

for i in range(2,n+1) :
    print(parent[i])


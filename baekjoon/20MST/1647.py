import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())

graph = []
parent = [0] * (n+1)
for i in range(1,n+1) :
    parent[i] = i

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b


for _ in range(m) :
    a,b,cost = map(int,input().split())
    graph.append((cost,a,b))

graph.sort()
result = 0
count = 0
for edge in graph :
    if count + 2 == n :
        break
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        result += cost
        count += 1


print(result)

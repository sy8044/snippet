import heapq
import itertools
from collections import deque
import collections
import sys

def input():
    return sys.stdin.readline().rstrip()

INF = int(1e10)
n, m, r = map(int,input().split())

item = list(map(int,input().split()))

adjlist = [[] for _ in range(n+1)]


for _ in range(r) :
    a,b,l = map(int,input().split())
    adjlist[a].append((b,l)) # b : node, l : length
    adjlist[b].append((a,l))

def dijkstra(start) :
    count = 0
    distance = [INF] * (n + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in adjlist[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    for i in range(1,n+1) :
        if distance[i] <= m :
            count += item[i-1]
    return count

result = []
for i in range(1,n+1) :
    result.append(dijkstra(i))

print(max(result))

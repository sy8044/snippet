import heapq
import itertools
from collections import deque
import collections
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int,input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            if graph[a][b] > graph[a][k]+graph[k][b] :
                graph[a][b] = graph[a][k] + graph[k][b]

for _ in range(m) :
    a,b,c = map(int,input().split())
    if graph[a-1][b-1] <= c :
        print("Enjoy other party")
    else :
        print("Stay here")

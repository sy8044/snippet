import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

adjmatrix = [list(map(int,input().split())) for _ in range(n)]


for i in range(n) :
    for a in range(n) :
        for b in range(n) :
            if adjmatrix[a][i] == 1 and adjmatrix[i][b] == 1 :
                adjmatrix[a][b] = 1


for row in adjmatrix:
    for col in row:
        print(col, end = " ")
    print()

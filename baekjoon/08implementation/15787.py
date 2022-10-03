import heapq
from collections import deque

import sys


def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())

train = [[0] * 20 for _ in range(n)]
for _ in range(m) :
    orders = list(map(int,input().split()))
    if orders[0] == 1 :
        train[orders[1]-1][orders[2]-1] = 1
    elif orders[0]== 2 :
        train[orders[1]-1][orders[2]-1] = 0
    elif orders[0]== 3:
        for i in range(19,0,-1) :
            train[orders[1]-1][i] = train[orders[1]-1][i-1]
        train[orders[1]-1][0] = 0
    elif orders[0]== 4 :
        for i in range(19) :
            train[orders[1]-1][i] = train[orders[1]-1][i+1]
        train[orders[1]-1][19] = 0

count = 0
state = []
for i in range(n) :
    if train[i] not in state :
        state.append(train[i])
        count += 1
print(count)

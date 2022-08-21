import heapq
from collections import deque

import sys

input = sys.stdin.readline

n, m = map(int,input().split())

bulb = list(map(int,input().split()))

for _ in range(m) :
    a , b ,c = map(int,input().split())
    if a == 1 :
        bulb[b-1] = c
    elif a == 2 :
        for i in range(b,c+1) :
            if bulb[i-1] == 0 :
                bulb[i-1] = 1
            else :
                bulb[i-1] = 0
    elif a == 3 :
        for i in range(b,c+1) :
            if bulb[i-1] == 1 :
                bulb[i-1] = 0
    elif a == 4 :
        for i in range(b,c+1) :
            if bulb[i-1] == 0 :
                bulb[i-1] = 1

print(*bulb)

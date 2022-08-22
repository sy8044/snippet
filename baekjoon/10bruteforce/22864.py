import heapq
from collections import deque

import sys

input = sys.stdin.readline

a,b,c,m = map(int,input().split())

count = 0
work = 0
if a > m :
    print(0)
else :
    for i in range(1,25) :
        if count + a <= m :
            count += a
            work += b
        else :
            if count - c >= 0 :
                count -= c
            else :
                count = 0
    print(work)

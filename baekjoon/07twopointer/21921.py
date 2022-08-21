import heapq
from collections import deque

import sys

input = sys.stdin.readline

n,x = map(int,input().split())

count = list(map(int,input().split()))

maxcount = 0
date = 1

maxcount = sum(count[0:x])
temp = maxcount
for i in range(x,n) :

    temp -= count[i-x]
    temp += count[i]
    if temp > maxcount :
        maxcount = temp
        date = 1
    elif temp == maxcount :
        date += 1

if maxcount == 0 :
    print("SAD")
else :
    print(maxcount)
    print(date)

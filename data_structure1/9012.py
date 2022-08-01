import heapq
from collections import deque

import sys

t = int(input())

for _ in range(t) :
    flag = True
    ll = input().rstrip()
    pcount = 0
    for i in ll :
        if i == '(' :
            pcount += 1
        elif i == ')' :
            pcount -= 1
        if pcount < 0 :
            flag = False
    if pcount == 0 and flag == True :
        print("YES")
    else :
        print("NO")

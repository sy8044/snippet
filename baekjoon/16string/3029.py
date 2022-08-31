import heapq
from collections import deque

import sys

input = sys.stdin.readline

now = list(map(int,input().split(':')))
time = list(map(int,input().split(':')))

if time[0] < now[0] :
    time[0] += 24

if time[2] < now[2] :
    time[2] += 60
    time[1] -= 1

if time[1] < now[1] :
    time[1] += 60
    time[0] -= 1
    
if time[0] == now[0] and time[1] == now[1] and time[2] == now[2] :
    print("24:00:00")
else :
    ans = [0,0,0]
    ans[2] = time[2] - now[2]
    ans[1] = time[1] - now[1]
    ans[0] = time[0] - now[0]
    
    for i in range(3) :
        if ans[i] < 10 :
            ans[i] = "0"+str(ans[i])
        else :
            str(ans[i])
    
    print(ans[0],ans[1],ans[2], sep=":")

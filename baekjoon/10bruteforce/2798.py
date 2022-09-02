import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int,input().split())

nums = list(map(int,input().split()))

nums.sort()

ans = -1
for i in range(0,n-2) :
    for j in range(i+1,n-1) :
        for l in range(j+1,n) :
            temp = nums[i]+nums[j]+nums[l]
            if ans < temp <= k:
                ans = temp
            else :
                continue


print(ans)

import heapq
from collections import deque

import sys
input = sys.stdin.readline

n,k = map(int,input().split())

nums = list(map(int,input().split()))

sums = 0

for i in range(k) :
    sums += nums[i]

maxsum = sums

for i in range(k,n) :
    sums += nums[i]
    sums -= nums[i-k]
    maxsum = max(sums,maxsum)

print(maxsum)

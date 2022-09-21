import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n,k = map(int,input().split())

nums = list(map(int,input().split()))

start, end = 0 , 0

if nums[0] % 2 == 0 :
    count = 0
    maxlen = 1
else :
    count = 1
    maxlen = 0

while end < n-1 :
    end += 1
    if nums[end] %2 != 0 :
        count += 1
        while count > k :
            if nums[start] % 2 != 0 :
                count -= 1
            start += 1
    maxlen = max(maxlen, end-start+1-count)

print(maxlen)

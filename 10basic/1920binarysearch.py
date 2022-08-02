import heapq
from collections import deque

import sys

n = int(input())

a = list(map(int,input().split()))

m = int(input())

nums = list(map(int,input().split()))

a.sort()

def binarySearch(start, end, target) :
    if start > end :
        print(0)
        return

    mid = (start+end) // 2
    if target > a[mid] :
        binarySearch(mid+1,end,target)
    elif target == a[mid] :
        print(1)
        return
    else :
        binarySearch(start,mid-1,target)

for i in nums :
    binarySearch(0,n-1,i)

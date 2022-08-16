import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

start = 1
end = n
q = 0
while start < end :
    mid = (start + end) // 2

    if mid ** 2 < n :
        start = mid + 1
    elif mid ** 2 >= n :
        end = mid - 1
print(start)

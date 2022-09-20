import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())

trees = list(map(int,input().split()))

ans = 0

start = 0
end = max(trees)

while start <= end :
    mid = (start+end) // 2
    cut = 0
    for tree in trees :
        if tree >= mid :
            cut += tree-mid

    if cut >= m :
        start = mid + 1
    else :
        end = mid - 1

print(end)

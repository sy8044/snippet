import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = int(input())


d = [0] * 21
d[1] = 1


for i in range(2,21) :
    d[i] = d[i-1] + d[i-2]

print(d[n])

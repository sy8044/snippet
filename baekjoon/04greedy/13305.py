import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

weight = list(map(int,input().split()))

price = list(map(int,input().split()))

min = price[0]
sum = 0

for i in range(n-1) :
    if min > price[i] :
        min = price[i]
    sum += (min * weight[i])

print(sum)

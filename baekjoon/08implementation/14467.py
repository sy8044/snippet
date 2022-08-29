import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

cow = [0] * 11
check = [False] * 11

count = 0
for _ in range(n) :
    num, pos = map(int,input().split())
    if check[num] == False :
        cow[num] = pos
        check[num] = True
    else :
        if cow[num] != pos :
            cow[num] = pos
            count += 1

print(count)


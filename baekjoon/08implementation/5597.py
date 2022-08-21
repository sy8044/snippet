import heapq
from collections import deque

import sys

input = sys.stdin.readline

check = [False] * 31

for _ in range(28) :
    num = int(input())
    check[num] = True

for i in range(1,31) :
    if check[i] == False :
        print(i)

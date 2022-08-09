import heapq
from collections import deque

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int, input().split()))

ll = a+b

answer = ' '.join(map(str, sorted(ll)))
print(answer)

import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

if n < 5 :
    if n % 2 != 0 :
        print(-1)
    else :
        print(n//2)
else :
    num = n % 5
    if num %2 == 0 :
        print(n//5+num//2)
    else :
        print((n//5)-1+(num+5)//2)

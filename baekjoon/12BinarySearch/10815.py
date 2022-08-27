import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

cards = list(map(int,input().split()))

m = int(input())
check = list(map(int,input().split()))

cards.sort()

for i in range(m) :
    start = 0
    end = n-1
    flag = False
    while start <= end :
        mid = (start + end) // 2
        if check[i] < cards[mid] :
            end = mid - 1
        elif check[i] > cards[mid] :
            start = mid + 1
        else :
            flag = True
            break
    if flag :
        print(1, end = ' ')
    else :
        print(0, end = ' ')

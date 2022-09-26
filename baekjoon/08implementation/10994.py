import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

size = 4 * n - 3

stars = [[' '] * size for _ in range(size)]

def draw(n,idx) :
    if n == 1 :
        stars[idx][idx] = '*'
        return

    l = 4 * n - 3
    for i in range(idx, l+idx) :
        stars[idx][i] = '*'
        stars[idx+l-1][i] = '*'
        stars[i][idx] = '*'
        stars[i][idx+l-1] = '*'

    draw(n-1,idx+2)

draw(n,0)

for i in range(size) :
    for j in range(size) :
        print(stars[i][j] , end = '')
    print()

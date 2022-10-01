import heapq
from collections import deque

import sys


def input():
    return sys.stdin.readline().rstrip()

t = int(input())

def rotate(arr, size) :
    mid = (size+1)//2
    temp =[ [0] * size for _ in range(size)]
    # 주 대각선 이동
    for i in range(size) :
        temp[i][mid-1] = arr[i][i]
    # 가운데 열 부대각선 이동
    for i in range(size) :
        temp[i][size-i-1] = arr[i][mid-1]
    # 부대각선을 가운데 행
    for i in range(size) :
        temp[mid-1][size-i-1] = arr[i][size-i-1]
    # 가운데 행을 주대각선 이동
    for i in range(size) :
        temp[i][i] = arr[mid-1][i]
    for i in range(size) :
        for j in range(size) :
            if temp[i][j] == 0 :
                temp[i][j] = arr[i][j]
    return temp

for _ in range(t) :
    n, d = map(int,input().split())
    arrayy = [list(map(int,input().split())) for _ in range(n)]
    if d < 0 :
        d += 360
    num = d // 45
    for _ in range(num) :
        arrayy = rotate(arrayy,n)
    for arr in arrayy :
        print(*arr)



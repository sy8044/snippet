import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

bingo = [list(map(int,input().split())) for _ in range(5)]

def getIndex(num) :
    for i in range(5) :
        for j in range(5) :
            if bingo[i][j] == num :
                return (i,j)

def checkRow(i) :
    for j in range(5) :
        if bingo[i][j] != 0 :
            return False
    return True

def checkCol(j) :

    for i in range(5) :
        if bingo[i][j] != 0 :
            return False
    return True

def checkDiagonal() :
    for i in range(5) :
        if bingo[i][i] != 0 :
            return False
    return True

def checkDiagonal2() :
    for i in range(5) :
        if bingo[i][4-i] != 0 :
            return False
    return True
ans = 0
count = 0
flag = True
while flag :
    nums = list(map(int,input().split()))
    for num in nums :
        i,j = getIndex(num)
        ans += 1
        bingo[i][j] = 0
        if checkRow(i) :
            count += 1
        if checkCol(j) :
            count += 1
        if i==j and checkDiagonal() :
            count += 1
        if i+j == 4 and checkDiagonal2() :
            count += 1
        if count >= 3 :
            flag = False
            break
    if not flag:
        break

print(ans)


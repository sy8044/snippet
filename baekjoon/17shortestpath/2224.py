# floyd
import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

x = int(input())

graph = [[0] * (52) for _ in range(52)]
# 0 : A


for _ in range(x) :
    frontIndex,backIndex = 0,0
    front, back = input().split(' => ')
    if ord(front) >= ord('a') :
        frontIndex = ord(front) - ord('a') + 26
    else :
        frontIndex = ord(front) - ord('A')
    if ord(back) >= ord('a') :
        backIndex = ord(back) - ord('a') + 26
    else :
        backIndex = ord(back) - ord('A')
    if frontIndex != backIndex:
        graph[frontIndex][backIndex] = 1


for k in range(52) :
    for a in range(52) :
        for b in range(52) :
            if graph[a][k] == 1 and graph[k][b] == 1  and a != b:
                graph[a][b] = 1

count = 0
ans = []
for a in range(52) :
    for b in range(52) :
        temp = ""
        if graph[a][b] == 1 and a!= b:
            count += 1
            if a < 26 :
                temp += chr(ord('A')+a)
            else :
                temp += chr(ord('a')+a-26)
            temp += " => "
            if b < 26 :
                temp += chr(ord('A')+b)
            else :
                temp += chr(ord('a')+b-26)
            ans.append(temp)

print(count)
for s in ans :
    print(s)
    


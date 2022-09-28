import heapq
from collections import deque

import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

dic = dict()
for _ in range(n) :
    name, extend = input().split('.')
    if extend in dic :
        dic[extend] += 1
    else :
        dic[extend] = 1

sortdic = sorted(dic.items())

for extend, count in sortdic :
    print(extend +" "+ str(count))


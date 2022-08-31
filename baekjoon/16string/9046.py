import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n) :
    words = input()
    dic = {}
    for letter in words :
        if letter == ' ' :
            continue
        if letter not in dic :
            dic[letter] = 1
        else :
            dic[letter] += 1
    new_total = list(dic.items())
    if len(new_total) == 1:
        print(new_total[0][0])
    else :
        new_total.sort(key=lambda x : (-x[1]))
        if new_total[0][1] == new_total[1][1] :
            print("?")
        else :
            print(new_total[0][0])


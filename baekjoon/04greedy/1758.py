import heapq
import itertools
from collections import deque
import collections
import sys

def input():
    return sys.stdin.readline().rstrip()


from collections import deque

n = int(input())

tips = [int(input()) for _ in range(n)]

tips.sort(reverse=True)
money = 0
for i in range(n) :
    temp = tips[i] - i
    if temp > 0 :
        money += temp

print(money)

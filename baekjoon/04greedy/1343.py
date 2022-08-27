import heapq
from collections import deque

import sys

input = sys.stdin.readline

words = input()

words = words.replace("XXXX", "AAAA")
words = words.replace("XX", "BB")

if 'X' in words :
    print(-1)
else :
    print(words)

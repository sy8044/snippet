import heapq
from collections import deque

import sys


def input():
    return sys.stdin.readline().rstrip()


words = list(input())

i = 0
start = 0
while i < len(words) :
    if words[i] == "<" :
        i += 1
        while words[i] != ">" :
            i += 1
        i+= 1
    elif words[i].isalnum() :
        start = i
        while i < len(words) and words[i].isalnum() :
            i+=1
        word = words[start:i]
        word.reverse()
        words[start:i] = word
    else :
        i+= 1

print("".join(words))



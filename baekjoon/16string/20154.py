import heapq
from collections import deque

import sys

def input():
    return sys.stdin.readline().rstrip()

words = input()

arr = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

def find(c) :
    num = ord(c)
    numA = ord('A')
    return num-numA

nums = []

for i in range(len(words)) :
    nums.append(arr[find(words[i])])

number = sum(nums) %10


if number % 2 == 1 :
    res = "I'm a winner!"
else :
    res = "You're the winner?"

print(res)

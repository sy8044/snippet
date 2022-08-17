import heapq
from collections import deque

import sys

input = sys.stdin.readline

n = input().strip()
ans = ""
arr = ["000","001","010","011","100","101","110","111"]
for letter in n :
    num = int(letter)
    ans += arr[num]

while ans[0] == "0" and len(ans) > 1 :
    ans = ans[1:]
print(ans)

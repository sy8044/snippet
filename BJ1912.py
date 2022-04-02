from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
num = list(map(int,input().split()))

sum = 0
maxx = 0
for i in range(k) :
    sum += num[i]
maxx = sum

for i in range(k,n) :
    sum += num[i]
    sum -= num[i-k]
    maxx = max(sum,maxx)

print(maxx)

import heapq
from collections import deque

import sys

input = sys.stdin.readline

start = int(input())

price = list(map(int,input().split()))

bnf = start
jstock = 0

triple = start
sstock = 0


for num in price :
    if bnf >= num :
        temp = bnf // num
        jstock += temp
        bnf -= (temp*num)

jmoney = price[13] * jstock + bnf

count = 0
flag = True # 상승 : true , 하락 : false

if price[1] < price[0] :
    flag = False
    count += 1
elif price[1] > price[0] :
    count += 1

for i in range(2,14) :
    if price[i] > price[i-1] :
        if flag :
            count += 1
        else :
            flag = True
            count = 1
    elif price[i] < price[i-1] :
        if flag :
            flag = False
            count = 1
        else :
            count += 1
    elif price[i] == price[i-1] :
        count = 0
    if count >= 3 :
        if flag and sstock > 0 :
            triple += (sstock*price[i])
            sstock = 0
        if not flag and triple > price[i] :
            temp = triple // price[i]
            sstock += temp
            triple -= (temp*price[i])

smoney = price[13] * sstock + triple

if jmoney > smoney :
    print("BNP")
elif jmoney == smoney :
    print("SAMESAME")
else :
    print("TIMING")

n = int(input())
count = 0
while n % 5 != 0 :
    n -= 3
    count += 1
    if n < 0 :
        print(-1)
        exit(0)

count += (n//5)

print(count)

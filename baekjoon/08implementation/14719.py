h, w = map(int,input().split())

wall = list(map(int,input().split()))

answer = 0
for i in range(1,w-1) :
    lmax = max(wall[:i])
    rmax = max(wall[i+1:])

    lower = min(lmax,rmax)

    if wall[i] < lower :
        answer += (lower - wall[i])

print(answer)

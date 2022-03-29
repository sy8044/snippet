from collections import deque

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x) :
    size = 1
    q = deque()
    q.append((y,x))
    while q :
        currentY, currentX = q.popleft()
        for direction in range(4) :
            nextY = currentY + dy[direction]
            nextX = currentX + dx[direction]
            if 0<= nextY < n and 0<= nextX < m :
                if graph[nextY][nextX] == 1 :
                    size += 1
                    graph[nextY][nextX] = 2
                    q.append((nextY,nextX))
    return size

count = 0
maxSize = 0

for j in range(n) :
    for i in range(m) :
        if graph[j][i] == 1 :
            graph[j][i] = 2
            count += 1
            maxSize = max(maxSize, bfs(j,i))
print(count)
print(maxSize)

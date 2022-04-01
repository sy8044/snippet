#bfs
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]

distance = [[-1]*m for _ in range(n)]

q = deque()

q.append([0,0])
distance[0][0] = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]

while q :
    currentY, currentX = q.popleft()
    for i in range(4) :
        nextY = currentY + dy[i]
        nextX = currentX + dx[i]
        if 0<= nextY < n and 0<= nextX< m :
            if distance[nextY][nextX] == -1 :
                if graph[nextY][nextX] == 0 :
                    distance[nextY][nextX] = distance[currentY][currentX]
                    q.appendleft([nextY,nextX])
                else :
                    distance[nextY][nextX] = distance[currentY][currentX] + 1
                    q.append([nextY,nextX])
print(distance[n-1][m-1])

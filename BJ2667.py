N = int(input())

graph = [list(map(int,input().strip())) for _ in range(N)]

#1이 있으면 dfs 후에 2로 변경
#크기 담는 변수
size = 0
#결과 담을 리스트
result = []

dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x) :
    global size
    size += 1
    currentY = y
    currentX = x
    for i in range(4) :
        nextY = currentY + dy[i]
        nextX = currentX + dx[i]
        if 0 <= nextY < N and 0<= nextX < N :
            if graph[nextY][nextX] == 1 :
                graph[nextY][nextX] = 2
                dfs(nextY,nextX)

#그래프 순환하며 1 찾기
for j in range(N) :
    for i in range(N) :
        if graph[j][i] == 1 : # 1이 있으면
            size = 0 # 크기 초기화
            graph[j][i] = 2 # 방문 표시
            dfs(j,i) # dfs통해 크기 찾기
            result.append(size) # 크기 리스트에 추가

result.sort()

print(len(result))
for i in result :
    print(i)


INF = int(1e9)

def input():
    return sys.stdin.readline().rstrip()

n,m = map(int,input().split())
start = int(input())
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost > distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1) :
    if distance[i] == INF :
        print("INFINITY")
    else :
        print(distance[i])

N, M = map(int,input().split())
result = []
visit = [False] * (N+1)

def backtrack(num) :
    if num == M :
        print(' '.join(map(str,result)))
        return
    for i in range(1, N+1) :
        if not visit[i]:
            visit[i] = True
            result.append(i)
            backtrack(num+1)
            visit[i] = False
            result.pop()

backtrack(0)

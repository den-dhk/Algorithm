t = int(input())
def dfs(visited, graph, x, length):
    global tmp
    tmp = max(tmp, length)
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(visited,graph,i,length+1)
    # 다른 경로에서도 지나갈 수 있기 때문에 방문처리를 취소해줌
    visited[x] = False


for tc in range(1,t+1):
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    result = 1
    for i in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    if m == 0:
        print(f'#{tc} {1}')
        continue
    tmp = 1
    for i in range(1,n+1):
        dfs(visited,graph,i,1)
        result = max(result, tmp)
    print(f'#{tc} {result}')


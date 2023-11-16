n,m = map(int, input().split())
visited = [False] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    u,v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(graph,x,visited):
    visited[x] = True
    for i in range(1,n+1):
        if graph[x][i] == 1 and not visited[i]:
            dfs(graph, i, visited)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)

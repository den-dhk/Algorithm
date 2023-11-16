from collections import deque

n,m,v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited_d = [False] * (n+1)
visited_b = [False] * (n+1)


for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1,n+1):
        if graph[v][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)

    
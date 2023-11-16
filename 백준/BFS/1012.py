from collections import deque

t = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = []

def bfs(graph,x,y,visited):
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

for i in range(t):
    m,n,k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited =[[False] * m for _ in range(n)]
    count = 0
    for i in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(graph,i,j,visited)
                count += 1
    result.append(count)

for i in result:
    print(i)
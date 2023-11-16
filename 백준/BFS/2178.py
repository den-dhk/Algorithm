from collections import deque

n,m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(graph, visited):
    queue = deque([(0,0)])
    visited[0][0] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] >= 1 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
    print(graph[n-1][m-1])

bfs(graph,visited)

# 주의 : cannot unpack non-iterable int object  => deque([(0,0)]),   deque([0,0]) 아님!
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = []
height = 0
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)
    height = max(height, max(a))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(graph,x,y,visited,h):
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
            
result = 0
for i in range(height+1):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[j][k]:
                count += 1
                bfs(graph, j, k, visited, i)
    result = max(result, count)
print(result)


'''
# dfs 런타임 에러
def dfs(graph,x,y,visited,h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] > h and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(graph,nx,ny,visited,h)
'''
from collections import deque

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input())))
visited = [[False] * n for _ in range(n)]

result = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(data,x,y,visited):
    count = 1
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if data[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    count += 1
    return count

for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and not visited[i][j]:
            result.append(bfs(data,i,j,visited))

result.sort()
print(len(result))
for i in result:
    print(i)
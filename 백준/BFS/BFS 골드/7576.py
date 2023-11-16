from collections import deque

m,n = map(int, input().split())
data = []
time = 0
queue = deque([])
visited = [[False] * m for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(len(data[i])):
        if data[i][j] == 1:
            queue.append((i,j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if data[nx][ny] == 0:
                queue.append((nx,ny))
                data[nx][ny] = data[x][y] + 1
check = True
result = max(map(max, data))
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            check = False
if not check:
    print(-1)
else:
    print(result-1)
from collections import deque

m,n,h = map(int, input().split())
graph = []
spaces = []

dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

check = False   # 익어있는 상태 확인용, 0 하나도 없으면 False => print(0)
check_m = True #  False = 못익은 게 존재
for k in range(h):
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
        for j in range(len(data[i])):
            if data[i][j] == 1:
                spaces.append((i,j,k))
            if data[i][j] == 0:
                check = True
    graph.append(data)

spaces = deque(spaces)
while spaces:
    x,y,z = spaces.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and nz >= 0 and nz < h:
            if graph[nz][nx][ny] == 0:
                spaces.append((nx,ny,nz))
                graph[nz][nx][ny] = graph[z][x][y] + 1

result = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                check_m = False
            result = max(result, graph[k][i][j])

# 모두 익어있는 상태
if not check_m:
    print(-1)
elif not check:
    print(0)
else:
    print(result-1)
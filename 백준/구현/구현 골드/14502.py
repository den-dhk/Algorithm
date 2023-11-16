from itertools import combinations


n,m = map(int, input().split())
graph = []
virus = []
space = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            space.append((i,j))
        if graph[i][j] == 2:
            virus.append((i,j))

result = -1e9

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread(x,y):
    # for i in range(4):
    #     nx = x + dx[i]
    #     ny = y + dy[i]
    #     if nx >= 0 and nx < n and ny >= 0 and ny < m:
    #         if graph[nx][ny] == 1 or graph[nx][ny] == 2:
    #             continue
    #         if graph[nx][ny] == 0:
    #             graph[nx][ny] = 2
    #             spread(nx,ny)
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if temp[x][y] == 0:
        temp[x][y] = 2
        spread(x-1,y)
        spread(x+1,y)
        spread(x,y-1)
        spread(x,y+1)
        return True
    return False
        
for cases in list(combinations(space, 3)):
    
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = graph[i][j]
    for case in cases:
        x,y = case
        temp[x][y] = 1

    for a,b in virus:
        temp[a][b] = 0
        spread(a,b)
    tmp = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                tmp += 1

    result = max(result, tmp)

print(result)
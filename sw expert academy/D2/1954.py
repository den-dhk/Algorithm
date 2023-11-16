t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = []

for i in range(t):
    n = int(input())
    table = [[0] * n for _ in range(n)]
    nx = 0
    ny = 0
    dir = 0
    count = 1
    while count <= (n*n):
        table[nx][ny] = count
        nx = nx + dx[dir]
        ny = ny + dy[dir]
        count += 1
        if nx < 0 or nx >= n or ny < 0 or ny >= n or table[nx][ny] != 0:
            nx = nx - dx[dir]
            ny = ny - dy[dir]
            dir = (dir + 1) % 4
            nx = nx + dx[dir]
            ny = ny + dy[dir]
        
    result.append(table)

for i in range(t):
    print(f'#{i+1}')
    for j in range(len(result[i])):
        for k in range(len(result[i][j])):
            print(result[i][j][k], end=' ')
        print()
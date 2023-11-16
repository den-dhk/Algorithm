import sys

input = sys.stdin.readline

n,m = map(int, input().split())
data = []
visited = [[0] * m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
r,c,d = map(int, input().split())
for i in range(n):
    data.append(list(map(int, input().split())))


result = 1
visited[r][c] = 1

while True:
    case_2 = 0
    for i in range(4):
        d = (d+3)%4
        nx = r + dx[d]
        ny = c + dy[d]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and data[nx][ny] == 0 and visited[nx][ny] == 0:
            r,c = nx, ny
            visited[r][c] = 1
            result += 1
            case_2 +=1
            break
    if case_2 == 0:
        nr = r - dx[d]
        nc = c - dy[d]
        if nr < 0 or nr >= n or nc < 0 or nc >= m or data[nr][nc] == 1:
            break
        r = nr
        c = nc

print(result)
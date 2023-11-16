from collections import deque

t = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for tc in range(1,t+1):
    n = int(input())
    mid = n // 2
    visited = [[False] * n for _ in range(n)]
    data = []
    for j in range(n):
        data.append(list(map(int,input())))
    result = 0
    q = deque([(mid,mid,0)])
    visited[mid][mid] = True
    while q:
        x,y,index = q.popleft()
        if index == mid:
            result += data[x][y]
        else:
            result += data[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,index+1))
    print(f'#{tc} {result}')
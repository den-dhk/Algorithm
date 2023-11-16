import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     graph.append(list(map(int, input().split())))

visited = [[-1] * m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    if visited[x][y] == -1:
        visited[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[x][y] > graph[nx][ny]:
                    visited[x][y] += dfs(nx,ny)
    return visited[x][y]

print(dfs(0,0))

# pypy3로 하면 메모리 초과, python3로 하면 바로 통과...? 
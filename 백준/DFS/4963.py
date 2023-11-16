import sys

input = sys.stdin.readline

dx = [-1,0,1,0,-1,-1,1,1]
dy = [0,1,0,-1,1,-1,1,-1]

def dfs(x,y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if graph[nx][ny] == 1:
            dfs(nx,ny)

result = []
while True:
    w,h = map(int, input().split())
    graph = []
    count = 0
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                dfs(i,j)
    result.append(count)

for i in result:
    print(i)

# visited로 체크하면서 dfs로 풀려고 했는데 런타임 에러 -> 방문한 좌표(graph[x][y])를 0으로 처리
# 재귀함수 사용 시에는 sys.setrecursionlimit(10000) 꼭 써주자
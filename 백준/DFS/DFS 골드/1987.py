r,c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input()))
# k = set()
visited = [0] * 26
result = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y,count):
    global result
    result = max(result, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and visited[ord(graph[nx][ny]) - ord('A')] == 0:
            visited[ord(graph[nx][ny]) - ord('A')] = 1
            dfs(nx,ny,count+1)
            visited[ord(graph[nx][ny]) - ord('A')] = 0

visited[ord(graph[0][0]) - ord('A')] = 1
dfs(0,0,1)
print(result)


    
    
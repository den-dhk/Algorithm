from collections import deque

n = int(input())
graph = []
visited_n = [[False] * n for _ in range(n)]
visited_d = [[False] * n for _ in range(n)]

for i in range(n):
    graph.append(list(map(str, input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs_normal(graph, x, y, visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    # 어떤 영역 찾는지
    now_area = graph[x][y]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if not visited[nx][ny] and graph[nx][ny] == now_area:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

def bfs_disabled(graph, x, y, visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    check = False
    area_a = ['R','G']
    # 어떤 영역 찾는지
    now_area = graph[x][y]
    if now_area in area_a:
        check = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if check:
                    if not visited[nx][ny] and graph[nx][ny] in area_a:
                        queue.append((nx,ny))
                        visited[nx][ny] = True
                else:
                    if not visited[nx][ny] and graph[nx][ny] == 'B':
                        queue.append((nx,ny))
                        visited[nx][ny] = True

count_n = 0
count_d = 0

for i in range(n):
    for j in range(n):
        if not visited_n[i][j]:
            bfs_normal(graph,i,j,visited_n)
            count_n += 1
        if not visited_d[i][j]:
            bfs_disabled(graph,i,j,visited_d)
            count_d += 1
print(count_n, count_d)

# bfs_disabled의 경우 check를 if로 빼주고 그에 따라 while문 하는 게 더 빠를듯...?  => 해보니까 시간 거의 똑같음
'''
def bfs_disabled(graph, x, y, visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    check = False
    area_a = ['R','G']
    # 어떤 영역 찾는지
    now_area = graph[x][y]
    if now_area in area_a:
        check = True
    if check:
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if check:
                        if not visited[nx][ny] and graph[nx][ny] in area_a:
                            queue.append((nx,ny))
                            visited[nx][ny] = True
    else:
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if not visited[nx][ny] and graph[nx][ny] == 'B':
                        queue.append((nx,ny))
                        visited[nx][ny] = True
'''
from collections import deque

n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

count = 0
queue = deque([1])
while queue:
    v = queue.popleft()
    visited[v] = True
    for i in range(1,n+1):
        if graph[v][i] == 1 and not visited[i]:
            queue.append(i)
            visited[i] = True
            count += 1

print(count)
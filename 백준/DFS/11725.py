import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for _ in range(n+1)]
visited=[0] * (n+1)
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def find_root(a):
    for i in graph[a]:
        if visited[i] == 0:
            visited[i] = a
            find_root(i)

find_root(1)

for i in range(2,n+1):
    print(visited[i])
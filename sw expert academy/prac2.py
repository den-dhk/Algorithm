t = int(input())
def row_find(i,j):
    global count
    a = 1
    while True:
        if graph[i][j+1] == 1:
            a += 1
            j += 1
        else:
            break
    if a == k:
        count += 1

def col_find(i,j):
    global count
    a = 1
    while True:
        if graph[i+1][j] == 1:
            a += 1
            i += 1
        else:
            break
    if a == k:
        count += 1

for tc in range(1,t+1):
    n,k = map(int, input().split())
    graph = [[0] * (n+2) for _ in range(n+2)]
    tmp = []
    count = 0
    for i in range(n):
        tmp.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            graph[i+1][j+1] = tmp[i][j]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j-1] == 0 and graph[i][j] == 1:
                row_find(i,j)
            if graph[i-1][j] == 0 and graph[i][j] == 1:
                col_find(i,j)
    print(f'#{tc} {count}')

    
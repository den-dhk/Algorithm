t = int(input())
count = []

for tc in range(1, t+1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[i][j] == 1:
                cnt += 1
            if data[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                if data[i][j] == 0:
                    cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if data[j][i] == 1:
                cnt += 1
            if data[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                if data[j][i] == 0:
                    cnt = 0
    count.append(result)

for i in range(t):
    print(f'#{i+1} {count[i]}')


'''
# 2회차
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
'''
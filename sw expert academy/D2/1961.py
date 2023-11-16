t = int(input())

def rotate(graph):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = graph[i][j]
    return result

for tc in range(1,t+1):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    print(f'#{tc}')
    a = []
    for i in range(1,4):
        graph = rotate(graph)
        a.append(graph)
    for i in range(n):
        for j in range(3):
            for k in range(n):
                print(a[j][i][k],end='')
            print(end=' ')
        print()

    
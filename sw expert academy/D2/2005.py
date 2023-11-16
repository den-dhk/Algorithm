t = int(input())

testcase = []
for i in range(t):
    n = int(input())
    testcase.append(n)

for i in range(t):
    n = testcase[i]
    result = [[0] * n for _ in range(n)]
    result[0][0] = 1
    for j in range(1, n):
        for k in range(j+1):
            if k == 0 or k == j:
                result[j][k] = 1
            else:
                result[j][k] = result[j-1][k-1] + result[j-1][k]

    print('#{}'.format((i+1)))
    for j in range(n):
        for k in range(n):
            if result[j][k] != 0:
                print(result[j][k], end=' ')
        print()

'''
#2회차
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = [[0] * i for i in range(1,n+1)]
    graph[0][0] = 1
    for i in range(1,n):
        for j in range(i+1):
            if j == 0:
                graph[i][j] = graph[i-1][j]
            elif j == i:
                graph[i][j] = graph[i-1][j-1]
            else:
                graph[i][j] = graph[i-1][j] + graph[i-1][j-1]
    print(f'#{tc}')
    for i in range(n):
        for j in range(i+1):
            print(graph[i][j], end=' ')
        print()
'''
def row_max(graph):
    answer = 0
    for i in range(100):
        answer = max(answer, sum(graph[i]))
    return answer

def col_max(graph):
    answer = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += graph[j][i]
        answer = max(answer, tmp)
    return answer

def diagonal(graph):
    answer1 = 0
    answer2 = 0
    for i in range(100):
        answer1 += graph[i][i]
        answer2 += graph[100-i-1][100-i-1]
    return max(answer1, answer2)


for tc in range(10):
    n = int(input())
    graph = []
    for i in range(100):
        graph.append(list(map(int, input().split())))
    result = max(row_max(graph), col_max(graph), diagonal(graph))
    print(f'#{n} {result}')
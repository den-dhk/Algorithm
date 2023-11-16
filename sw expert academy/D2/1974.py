# 못품 -> 참조 사이트 : https://hose0728.tistory.com/23
t = int(input())

def find_row(graph):
    global check
    for i in range(9):
        c = set()
        for j in range(9):
            if graph[i][j] not in c:
                c.add(graph[i][j])
            else:
                check = False
                break
def find_col(graph):
    global check
    for i in range(9):
        c = set()
        for j in range(9):
            if graph[j][i] not in c:
                c.add(graph[j][i])
            else:
                check = False
                break
def find(graph, x, y):
    global check
    c = set()
    for i in range(x,x+2):
        for j in range(y,y+2):
            if graph[i][j] not in c:
                c.add(graph[i][j])
            else:
                check = False
                break
for tc in range(1,t+1):
    graph = []
    check = True
    for i in range(9):
        graph.append(list(map(int, input().split())))
    find_row(graph)
    find_col(graph)
    for i in range(0,9,3):
        for j in range(0,9,3):
            find(graph,i,j)
    if check:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
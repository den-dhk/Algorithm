# w : 가로 길이,  h : 세로 길이
# park : 공원을 나타내는 문자열 배열
# routes : 로봇 강아지가 수행할 명령이 담긴 문자열 배열

park = ["SOO","OXX","OOO"]
routes = ["E 2","S 2","W 1"]
# result = [0,1]

def solution(park, routes):
    data = [[0] * len(park[0]) for _ in range(len(park))]

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x,y = i,j
            data[i][j] = park[i][j]

    direction = ['N', 'S', 'W', 'E']
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    routes = [[routes[i][0], int(routes[i][-1])] for i in range(len(routes))]

    for i in routes:
        for j in range(4):
            if i[0] == direction[j]:
                nx,ny = x,y
                for k in range(i[1]):
                    nx += dx[j]
                    ny += dy[j]
                    if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]) or park[nx][ny] == 'X':
                        nx = x
                        ny = y
                        break
                x,y = nx,ny

    answer = [x,y]
    return answer

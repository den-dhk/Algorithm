t = int(input())
result = []

for i in range(t):
    n = int(input())
    speed = 0
    distance = 0
    for j in range(n):
        data = list(map(int, input().split()))
        if data[0] == 0:
            distance += speed
        elif data[0] == 1:
            speed += data[1]
            distance += speed
        elif data[0] == 2:
            speed -= data[1]
            if speed < 0:
                speed = 0
            distance += speed
    result.append(distance)

for i in range(t):
    print(f'#{i+1} {result[i]}')


'''
#2회차
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    result = 0
    speed = 0
    for i in range(n):
        data = list(map(int, input().split()))
        if data[0] == 1:
            speed += data[1]
        elif data[0] == 2:
            speed -= data[1]
        elif data[0] == 0:
            pass
        if speed > 0:
            result += speed
        else:
            speed = 0
    print(f'#{tc} {result}')
'''
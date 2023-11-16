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
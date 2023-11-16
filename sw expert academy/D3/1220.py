# N : 1,   S : 2
for tc in range(1,11):
    n = int(input())
    data = []
    count = 0
    for i in range(100):
        data.append(list(map(int, input().split())))
    # 1이 먼저 나와야됨
    for j in range(100):
        check = False
        for i in range(100):
            if data[i][j] == 1:
                check = True
            if check and data[i][j] == 2:
                count += 1
                check = False
    print(f'#{tc} {count}')
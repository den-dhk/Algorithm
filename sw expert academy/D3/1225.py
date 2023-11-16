from collections import deque

for tc in range(1,11):
    n = int(input())
    data = list(map(int, input().split()))
    data =deque(data)
    index = 1
    while True:
        if index == 6:
            index = 1
        data[0] = data[0]-index
        data.rotate(-1)
        if data[-1] <= 0:
            data[-1] = 0
            break
        index += 1
    print(f'#{n}', end='')
    print(' ', end='')
    for i in data:
        print(i, end=' ')
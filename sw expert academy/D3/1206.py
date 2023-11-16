for tc in range(1,11):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0
    for i in range(2,len(data)-2):
        count = max(data[i-2], data[i-1], data[i+1], data[i+2])
        if data[i] > count:
            result += data[i] - count
    print(f'#{tc} {result}')
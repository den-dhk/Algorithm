t = int(input())

for tc in range(1,t+1):
    n = int(input())
    data = list(map(int, input().split()))
    d = [0 for _ in range(101)]
    for i in data:
        d[i] += 1
    result = max(d)
    for i in range(len(d)-1,-1,-1):
        if d[i] == result:
            result = i
            break
    print(f'#{tc} {result}')
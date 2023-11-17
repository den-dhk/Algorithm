t = int(input())

for tc in range(1,t+1):
    n = int(input())
    data = list(map(int, input().split()))
    data = [abs(i) for i in data]
    k = min(data)
    count = 0
    for i in data:
        count += 1 if i == k else 0
    print(f'#{tc} {k} {count}')
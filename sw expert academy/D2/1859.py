# insight : 뒤에부터 계산해서 더해도 됨
t = int(input())
answer = []
for _ in range(t):
    result = 0
    n = int(input())
    data = list(map(int, input().split()))
    best_price = data[-1]
    for j in range(n-1,-1,-1):
        if best_price > data[j]:
            result += best_price - data[j]
        elif best_price < data[j]:
            best_price = data[j]
    answer.append(result)

for i in range(t):
    print(f'#{i+1} {answer[i]}')

t = int(input())
result = []
for i in range(t):
    sum = 0
    a = list(map(int, input().split()))
    for j in a:
        sum += j
    result.append(sum/len(a))
for i in range(t):
    print(f'#{i+1} {round(result[i])}')
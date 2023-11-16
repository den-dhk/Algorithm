tc = int(input())
result = []
for _ in range(tc):
    n = int(input())
    data = []
    for i in range(n):
        a,b = map(int, input().split())
        data.append((a,b))
    data.sort(key=lambda x: x[0])
    low_rank = data[0][1]
    count = 1
    for i in range(1,n):
        if data[i][1] < low_rank:
            count += 1
            low_rank = data[i][1]
    result.append(count)

for i in result:
    print(i)
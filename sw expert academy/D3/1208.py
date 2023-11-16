for i in range(1,11):
    dump = int(input())
    data = list(map(int, input().split()))
    for j in range(dump):
        high = max(data)
        h_index = data.index(high)
        low = min(data)
        l_index = data.index(low)
        data[h_index] -= 1
        data[l_index] += 1
    result = max(data) - min(data)
    print(f'#{i} {result}')

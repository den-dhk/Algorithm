t = int(input())
mul = [2,3,5,7,11]
result = []
for i in range(t):
    n = int(input())
    a = 0
    count = [0] * len(mul)
    sum = 0
    while a < len(mul):
        if n % mul[a] != 0:
            count[a] = sum
            a += 1
            sum = 0
        else:
            n = n // mul[a]
            sum += 1
    result.append(count)
        
for i in range(t):
    print(f'#{i+1}', end=' ')
    for j in result[i]:
        print(j, end=' ')
    print()
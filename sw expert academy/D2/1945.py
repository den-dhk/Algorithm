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


'''
# 2회차
t = int(input())
n_list = [2,3,5,7,11]

for tc in range(1,t+1):
    n = int(input())
    result = []
    for i in n_list:
        count = 0
        while True:
            if n % i == 0:
                count += 1
                n = n // i
            else:
                break
        result.append(count)
    print(f'#{tc}', end=' ')
    for i in result:
        print(i, end=' ')
    print()
'''
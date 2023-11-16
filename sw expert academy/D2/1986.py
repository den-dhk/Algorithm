t = int(input())
result = []

for i in range(t):
    a = int(input())
    b = 0
    for j in range(1,a+1):
        if j % 2 == 0:
            b -= j
        else:
            b += j
    result.append(b)

for i in range(t):
    print(f'#{i+1} {result[i]}')


'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    result = 0
    for i in range(1,n+1):
        result += i if i % 2 != 0 else -i
    print(f'#{tc} {result}')
'''
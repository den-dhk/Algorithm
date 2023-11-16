t = int(input())
result = []

for i in range(t):
    a = list(map(int, input().split()))
    b = a[0]
    for j in a:
        if b < j:
            b = j
    result.append(b)

for i in range(t):
    print(f'#{i+1} {result[i]}')


'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    data = list(map(int, input().split()))
    print(f'#{tc} {max(data)}')
'''
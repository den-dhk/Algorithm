t = int(input())
result = []

for i in range(t):
    b = int(input())
    a = list(map(int, input().split()))
    a.sort()
    result.append(a)

for i in range(t):
    print(f'#{i+1} ', end='')
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()

'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()
    print(f'#{tc} ', end='')
    for i in data:
        print(i, end=' ')
    print()
'''
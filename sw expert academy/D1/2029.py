t = int(input())
m = []
n = []
for i in range(t):
    a,b = map(int, input().split())
    m.append(a // b)
    n.append(a % b)
for i in range(t):
    print(f'#{i+1} {m[i]} {n[i]}')


'''
# 2회차
t = int(input())
for tc in range(1,t+1):
    a,b =map(int, input().split())
    m = a // b
    n = a % b
    print(f'#{tc} {m} {n}')
'''
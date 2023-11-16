t = int(input())
result = []

for i in range(t):
    a = list(map(int, input().split()))
    b = []
    b.append(a[0] + a[2])
    b.append(a[1] + a[3])

    if b[1] >= 60:
        b[0] = b[0] + (b[1] // 60)
        b[1] = b[1] % 60
    if b[0] > 12:
        b[0] = b[0] - 12                   # b[0] = b[0] % 12하면 안됨!
    
    result.append([b[0], b[1]])

for i in range(t):
    print(f'#{i+1} {result[i][0]} {result[i][1]}')

'''
# 2 번째 풀이
t = int(input())
data = []

for tc in range(t):
    h1,m1,h2,m2 = map(int, input().split())
    h = (h1 + h2)
    if h > 12:
        if h % 12 == 0:
            h = 12
        else:
            h = h % 12
    m = m1 + m2
    if m >= 60:
        h += m // 60
        m = m % 60
    data.append((h,m))

for i in range(t):
    print(f'#{i+1} {data[i][0]} {data[i][1]}')
'''

'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    h1,m1,h2,m2 = map(int, input().split())
    m = (m1 + m2) % 60
    h = (((m1+m2) // 60) + h1 + h2)
    h = h if h <= 12 else h % 13 + 1
    print(f'#{tc} {h} {m}')
'''
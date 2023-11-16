t = int(input())
result = []

for i in range(t):
    n, m = map(int, input().split())

    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    a = 0
    a_max = 0
    if n > m:
        for j in range(n-m+1):
            for k in range(m):
                a += (n_list[j+k] * m_list[k])
            if a_max < a:
                a_max = a
            a = 0
    elif n < m:
        for j in range(m-n+1):
            for k in range(n):
                a += (m_list[j+k] * n_list[k])
            if a_max < a:
                a_max = a
            a = 0
    else:
        for j in range(n):
            a += (n_list[j] * m_list[j])
        a_max = a

    result.append(a_max)

for i in range(t):
    print(f'#{i+1} {result[i]}')


'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    if n > m:
        for i in range(n-m+1):
            tmp = 0
            for j in range(m):
                tmp += a[i+j] * b[j]
            result = max(result, tmp)
    elif n < m:
        for i in range(m-n+1):
            tmp = 0
            for j in range(n):
                tmp += a[j] * b[i+j]
            result = max(result, tmp)
    else:
        tmp = 0
        for i in range(n):
            for i in range(n):
                tmp += a[j] * b[j]
        result = max(result, tmp)
    print(f'#{tc} {result}')
'''
t= int(input())
result = []

for i in range(t):
    n, m = map(int, input().split())
    r_max = 0
    storage = []
    for j in range(n):
        storage.append(list(map(int, input().split())))

    for k in range(n-m+1):
        for a in range(n-m+1):
            m_max = 0
            for b in range(m):
                for c in range(m):
                    m_max += storage[k+b][a+c]      # 3개일 때 바꿀 것
            if r_max < m_max:
                r_max = m_max
    result.append(r_max)

for i in range(t):
    print(f'#{i+1} {result[i]}')

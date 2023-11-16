t = int(input())

for tc in range(1,t+1):
    h1,m1,h2,m2 = map(int, input().split())
    m = (m1 + m2) % 60
    h = (((m1+m2) // 60) + h1 + h2)
    h = h if h <= 12 else h % 13 + 1
    print(f'#{tc} {h} {m}')
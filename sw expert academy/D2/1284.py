t = int(input())

for tc in range(1,t+1):
    p,q,r,s,w = map(int, input().split())
    # a : 1L * p,   b : 기본 요금 q, if r 이하,  else 1L * s
    # w : 한달 수도 사용량
    a = w * p
    if w <= r:
        b = q
    else:
        b = q + (w-r) * s
    print(f'#{tc} {a if a < b else b}')
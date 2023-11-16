# https://jennnn.tistory.com/4

t = int(input())
# m초에 k개 생산
for tc in range(1,t+1):
    n,m,k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    result = "Possible"

    for i in range(n):
        boong = (data[i] // m) * k - (i+1)
        if boong < 0:
            result = "Impossible"
            break
    print('#{} {}'.format(tc, result))
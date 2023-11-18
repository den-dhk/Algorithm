for tc in range(1,11):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0
    for i in range(2,len(data)-2):
        count = max(data[i-2], data[i-1], data[i+1], data[i+2])
        if data[i] > count:
            result += data[i] - count
    print(f'#{tc} {result}')

'''
# 2회차
for tc in range(1,11):
    n = int(input())
    data = list(map(int, input().split()))
    result = 0
    for i in range(2,n-2):
        m = data[i-2:i+3]
        if data[i] == max(m):
            m.sort()
            result += data[i]-m[-2]
    print(f'#{tc} {result}')
'''
t = int(input())
result = []
for i in range(t):
    a = list(map(int, input().split()))
    hap = 0
    m = max(a)
    n = min(a)
    for j in a:
        if j == m or j == n:
            hap
        else:
            hap += j
    result.append(round((hap / (len(a) - 2))))

for i in range(t):
    print('#{0} {1}'.format(i+1, result[i]))

'''
# 두 번째 풀이
t = int(input())
result = []
for i in range(t):
    data = list(map(int, input().split()))
    a = max(data)
    b = min(data)
    count = round((sum(data) - a - b) // (len(data)-2))
    result.append(count)

for i in range(t):
    print(f'#{i+1} {result[i]}')
'''


'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    data = list(map(int, input().split()))
    data.pop(data.index(max(data)))
    data.pop(data.index(min(data)))
    print(f'#{tc} {round(sum(data)/len(data))}')
'''
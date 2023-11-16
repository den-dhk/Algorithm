t = int(input())

for tc in range(1,t+1):
    x = input()
    count = 0
    if x[0] == '1':
        count += 1
    for i in range(1,len(x)):
        if x[i-1] != x[i]:
            count += 1
    print(f'#{tc} {count}')

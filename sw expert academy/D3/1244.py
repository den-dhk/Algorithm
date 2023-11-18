def dfs(index, count):
    global result
    if count == int(cnt):
        result = max(int(''.join(data)), result)
        return
    for now in range(index, len(data)):
        for max_idx in range(now+1, len(data)):
            if data[now] <= data[max_idx]:
                data[now], data[max_idx] = data[max_idx], data[now]
                dfs(now, count + 1)
                data[now], data[max_idx] = data[max_idx], data[now]
    if result == 0 and count < int(cnt):
        extra = (int(cnt) - count) % 2
        if extra == 1:
            data[-1], data[-2] = data[-2], data[-1]
        dfs(index, int(cnt))

t = int(input())

for tc in range(1, t+1):
    data, cnt = input().split()
    data = list(data)
    result = 0
    dfs(0,0)
    print(f'#{tc} {result}')
    
'''
for tc in range(1,int(input())+1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(tc,max(map(int,now))))
'''
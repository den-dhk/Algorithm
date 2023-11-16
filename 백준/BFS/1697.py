from collections import deque

n,k = map(int, input().split())
MAX = 100001
d = [0] * MAX
q = deque([n])
while q:
    x = q.popleft()
    if x == k:
        print(d[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx < MAX and not d[nx]:
            d[nx] = d[x] + 1
            q.append(nx)


    


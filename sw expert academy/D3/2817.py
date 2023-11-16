t = int(input())

def dfs(data,index,answer,k):
    global count
    if index >= n:
        return
    if (answer+data[index]) == k:
        count += 1
    if (answer+data[index]) < k:
        dfs(data, index+1, answer+data[index], k)
    dfs(data, index+1, answer, k)



for i in range(1,t+1):
    n,k = map(int, input().split())
    data = list(map(int, input().split()))
    count = 0
    dfs(data, 0, 0, k)
    print(f'#{i} {count}')


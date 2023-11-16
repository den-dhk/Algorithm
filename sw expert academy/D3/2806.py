# https://cheon2308.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-9663%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-N-Queen

n = int(input())
row = [0] * n
result = 0

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x+1)

dfs(0)
print(result)
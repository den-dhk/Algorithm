from itertools import combinations

t = int(input())

for tc in range(1,t+1):
    n,l = map(int, input().split())
    data = []
    for i in range(n):
        score,cal = map(int, input().split())
        data.append((score,cal))
    result = 0
    for i in range(1,n+1):
        for cases in list(combinations(data, i)):
            tmp = 0
            t_cal = 0
            for case in cases:
                score, cal = case
                tmp += score
                t_cal += cal
            if t_cal > l:
                continue
            result = max(result, tmp)
    print(f'#{tc} {result}')


# DFS로도 풀어보기 : https://whitehairhan.tistory.com/343

'''
t = int(input())

def dfs(index, sTaste, sKcal):
    global maxTaste

    if sKcal > l:
        return 
    
    if maxTaste < sTaste:
        maxTaste = sTaste

    if index == n:
        return
    
    taste, kcal = data[index]

    dfs(index+1, sTaste+taste, sKcal+kcal)
    dfs(index+1, sTaste, sKcal)

for tc in range(1,t+1):
    n,l = map(int, input().split())
    data = []
    for i in range(n):
        score,cal = map(int, input().split())
        data.append((score,cal))
    
    maxTaste = 0
    dfs(0,0,0)

    print(f"#{tc} {maxTaste}")
'''
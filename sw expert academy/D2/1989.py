t = int(input())
result = []

for i in range(t):
    a = str(input())
    b = a[::-1]
    if a[:(len(a) // 2)] == b[:(len(a) // 2)]:
        result.append(1)
    else:
        result.append(0)

for i in range(t):
    print(f'#{i+1} {result[i]}')

'''
#2회차
t = int(input())

for tc in range(1,t+1):
    check = True
    s = input()
    l = len(s)
    mid = l // 2
    for i in range(mid):
        if s[i] != s[l-1-i]:
            check = False
            break
    if check:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
'''
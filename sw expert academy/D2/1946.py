t = int(input())
result = []

for tc in range(t):
    n = int(input())
    c = ''
    for i in range(n):
        a,b = input().split()
        b = int(b)
        c = c + (a*b)
    result.append(c)

for i in range(t):
    print(f'#{i+1}')
    count = 0
    a = len(result[i])
    for j in range((a // 10)+1):
        if (count+9) > a:
            print(result[i][count:len(result[i])])
            break
        print(result[i][count:count+10])
        count += 10
    
'''
#2회차
t = int(input())

for tc in range(1,t+1):
    n = int(input())
    result = ''
    for _ in range(n):
        a,b = input().split()
        result += a * int(b)
    print(f'#{tc}')
    for i in range(0,len(result), 10):
        print(result[i:i+10])
'''
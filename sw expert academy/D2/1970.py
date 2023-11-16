t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
result = []

for i in range(t):
    a = int(input())
    b = []
    for j in range(len(money)):
        b.append((a // money[j]))
        a = a % money[j]
    result.append(b)

for i in range(t):
    print(f'#{i+1}')
    for j in range(8):
        print(result[i][j], end=' ')
    print()

'''
# 2회차
t = int(input())
money = [50000,10000,5000,1000,500,100,50,10]
for tc in range(1,t+1):
    n = int(input())
    result = []
    for i in money:
        result.append(n//i)
        n = n % i

    print(f'#{tc}')
    for i in result:
        print(i, end=' ')
    print()
'''
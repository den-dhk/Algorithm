a = int(input())
b = []

for i in range(1,a+1):
    if a % i == 0:
        b.append(i)

for j in b:
    print(j, end=' ')


'''
# 2회차
n = int(input())
result = []
for i in range(1,n+1):
    if n % i == 0:
        result.append(i)

for i in result:
    print(i, end=' ')
'''
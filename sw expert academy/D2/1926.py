t = int(input())

for i in range(1, t+1):
    count = 0
    for j in range(len(str(i))):
        if '3' == str(i)[j] or '6' == str(i)[j] or '9' == str(i)[j]:
            count += 1
    if count > 0:
        print(count*'-', end='')
        print(end=' ')
    else:
        print(i, end=' ')


'''
# 2회차
n = int(input())

for i in range(1,n+1):
    a = str(i)
    check = False
    c = 0
    for j in a:
        if j in ['3','6','9']:
            check = True
            c += 1
    if check:
        print('-'*c, end=' ')
    else:
        print(i, end=' ')
'''
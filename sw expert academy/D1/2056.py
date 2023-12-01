t = int(input())
a = []
for i in range(t):
    a.append(str(input()))
num = 0
for i in a:
    if len(i) != 8:
        print(f'#5{num+1} -1')
    if int(i[4:6]) >= 1 and int(i[4:6]) <= 12:
        if int(i[4:6]) == 2:
            if int(i[6:8]) >= 1 and int(i[6:8]) <= 28:
                print(f'#{num+1} {i[:4]}/{i[4:6]}/{i[6:8]}') 
            else:
                print(f'#{num+1} -1')
        elif int(i[4:6]) == 1 or int(i[4:6]) == 3 or int(i[4:6]) == 5 or int(i[4:6]) == 7 or int(i[4:6]) == 8 or int(i[4:6]) == 10 or int(i[4:6]) == 12:
            if int(i[6:8]) >= 1 and int(i[6:8]) <= 31:
                print(f'#{num+1} {i[:4]}/{i[4:6]}/{i[6:8]}')
            else:
                print(f'#{num+1} -1')
        elif int(i[4:6]) == 4 or int(i[4:6]) == 6 or int(i[4:6]) == 9 or int(i[4:6]) == 11:
            if int(i[6:8]) >= 1 and int(i[6:8]) <= 30:
                print(f'#{num+1} {i[:4]}/{i[4:6]}/{i[6:8]}')
            else:
                print(f'#{num+1} -1')
    else:
        print(f'#{num+1} -1')
    num += 1


'''
# 2회차
t = int(input())

for tc in range(1,t+1):
    n = input()
    m = int(n[4:6])
    d = int(n[6:8])
    check = True
    m_31 = [1,3,5,7,8,10,12]
    m_30 = [4,6,9,11]
    if m < 1 or m > 12:
        check = False
    if m in m_31:
        if d < 1 or d > 31:
            check = False
    elif m in m_30:
        if d < 1 or d > 30:
            check = False
    elif m == 2:
        if d < 1 or d > 28:
            check = False
    if check:
        print(f'#{tc} {n[:4]}/{n[4:6]}/{n[6:8]}')
    else:
        print(f'#{tc} {-1}')
'''
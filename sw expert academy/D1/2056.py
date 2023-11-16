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
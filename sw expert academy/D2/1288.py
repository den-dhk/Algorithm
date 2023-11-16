t = int(input())

for tc in range(1,t+1):
    n = int(input())
    count = 0
    index = 1
    k = index * n
    c_list = set()
    while True:
        count += 1
        k = str(k)
        for i in range(len(k)):
            c_list.add(int(k[i]))
        if len(c_list) == 10:
            break
        index += 1
        k = int(k)
        k = index * n
    
    print(f'#{tc} {count * n}')
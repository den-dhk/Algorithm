def check_y(x,y,n):
    for i in range(n//2):
        if data[x][y+i] != data[x][y+n-i-1]:
            return False
    return True

def check_x(x,y,n):
    for i in range(n//2):
        if data[x+i][y] != data[x+n-i-1][y]:    
            return False
    return True


for tc in range(1,11):
    n = int(input())
    data = []
    for i in range(8):
        data.append(list(input()))
    count = 0
    for i in range(8):
        for j in range(8-n+1):
            if check_y(i,j,n):
                count += 1

    for i in range(8-n+1):
        for j in range(8):
            if check_x(i,j,n):
                count += 1
    print(f'#{tc} {count}')

    

    
    
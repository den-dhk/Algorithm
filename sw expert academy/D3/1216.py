# 가로 짝수
def row_even_find(x,y,index):
    global result
    if data[x][y-index] == data[x][y+1+index]:
        result = max(result, (index+1)*2)
        if y-(index+1) >= 0 and y+1+(index+1) < 100:
            row_even_find(x,y,index+1)
        else:
            return
    else:
        return
    
# 가로 홀수
def row_odd_find(x,y,index):
    global result
    if data[x][y-index] == data[x][y+index]:
        result = max(result, index*2+1)
        if y-(index+1) >= 0 and y+(index+1) < 100:
            row_odd_find(x,y,index+1)
        else:  
            return
    else:
        return 

# 세로 짝수
def col_even_find(x,y,index):
    global result
    if data[x-index][y] == data[x+1+index][y]:
        result = max(result, (index+1)*2)
        if x-(index+1) >= 0 and x+1+(index+1) < 100:
            col_even_find(x,y,index+1)
        else:
            return
    else:
        return

# 세로 홀수
def col_odd_find(x,y,index):
    global result
    if data[x-index][y] == data[x+index][y]:
        result = max(result, index*2+1)
        if x-(index+1) >= 0 and x+(index+1) < 100:
            col_odd_find(x,y,index+1)
        else:  
            return
    else:
        return 

for tc in range(1,11):
    t = int(input())
    data = []
    result = 1
    for i in range(100):
        data.append(list(input()))
    for i in range(100):
        for j in range(99):
            row_even_find(i,j,0)
            row_odd_find(i,j,1)
    for i in range(99):
        for j in range(100):
            col_even_find(i,j,0)
            col_odd_find(i,j,1)
    print(f'#{t} {result}')
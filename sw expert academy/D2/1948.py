from datetime import datetime

def calculate_date(date_list):
    day1 = datetime(year=2021, month=date_list[0], day=date_list[1])
    day2 = datetime(year=2021, month=date_list[2], day=date_list[3])

    return (day2-day1).days + 1

t = int(input())
result = []
for idx in range(t):
    date_list = list(map(int, input().split()))
    result.append(calculate_date(date_list))

for i in range(t):
    print(f'#{idx+1} {result[i]}')


'''
#2회차
t = int(input())
data = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for tc in range(1,t+1):
    m1,d1,m2,d2 = map(int, input().split())
    result = 0
    if m2-m1 > 1:
        result += data[m1] - d1 + 1
        result += d2
        for i in range(m1+1,m2):
            result += data[i]
    elif m2-m1 == 1:
        result += data[m1] - d1 + 1
        result += d2
        result+=1
    else:
        result += d2-d1 + 1
    print(f'#{tc} {result}')
'''
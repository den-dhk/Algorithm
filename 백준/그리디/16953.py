a,b = map(int, input().split())
count = 1
while a < b:
    if str(b)[-1] == '1':
        b = str(b)
        b = b[:-1]
        b = int(b)
        count += 1
    elif b % 2 == 0:
        b = b // 2
        count += 1
    else:
        break
if a == b:
    print(count)
else:
    print(-1)
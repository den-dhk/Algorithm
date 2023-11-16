d = [False] * 10001

for i in range(1,10001):
    k = i
    i = str(i)
    for j in i:
        k += int(j)
    if k <= 10000:
        d[k] = True

for i in range(1,10001):
    if d[i] is False:
        print(i)
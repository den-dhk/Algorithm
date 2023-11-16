import math

n = int(input())
d = [0] * 10
n = str(n)
for i in range(len(n)):
    if int(n[i]) == 9:
        d[6] += 1
    else:
        d[int(n[i])] += 1
d[6] = math.ceil(d[6] / 2)
print(max(d))
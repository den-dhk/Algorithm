n = int(input())

d = [5001] * (n+1)
option = [3,5]

d[0] = 0
for i in range(2):
    for j in range(option[i], n+1):
        d[j] = min(d[j], d[j-option[i]]+1)

if d[n] == 5001:
    print(-1)
else:
    print(d[n])
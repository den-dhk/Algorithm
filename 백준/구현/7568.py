import sys

input = sys.stdin.readline
data = []

n = int(input())
for i in range(n):
    data.append(list(map(int, input().split())))

result = []
for i in range(n):
    tmp = 1
    w,h = data[i]
    for j in range(n):
        if i == j:
            continue
        if w < data[j][0] and h < data[j][1]:
            tmp += 1
    result.append(tmp)

for i in result:
    print(i, end=' ')
        

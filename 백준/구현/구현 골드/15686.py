import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int, input().split())
data = []
house = []
chicken = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 2:
            chicken.append((i,j))
        if data[i][j] == 1:
            house.append((i,j))

result = 1e9
for cases in list(combinations(chicken, m)):
    total = 0
    for x,y in house:
        min_value = 1e9
        for i,j in cases:
            min_value = min(min_value, abs(x-i)+abs(y-j))
        total += min_value
    result = min(result, total)

print(result)
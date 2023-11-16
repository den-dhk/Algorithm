import sys

input = sys.stdin.readline

n = int(input())
data = [[0] * 101 for _ in range(101)]
for i in range(n):
    x,y = map(int, input().split())
    for row in range(x,x+10):
        for col in range(y,y+10):
            data[row][col] = 1

count = 0
for i in range(1,101):
    for j in range(1,101):
        if data[i][j] == 1:
            count += 1

print(count)
    
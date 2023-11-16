import sys

input = sys.stdin.readline

k = int(input())
result = []
for _ in range(k):
    i = int(input())
    if i == 0:
        result.pop()
        continue
    result.append(i)

print(sum(result))
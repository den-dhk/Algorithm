n = int(input())
data = list(map(int, input().split()))
data.sort()

sum = 0
result = 0
for i in data:
    sum += i
    result += sum

print(result)
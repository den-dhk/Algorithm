n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)
result = int(data[n-1] * n)

for i in range(n):
    result = max(result, int(data[i] * (i+1)))

print(result)

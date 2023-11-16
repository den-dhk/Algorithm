import heapq

n = int(input())
data = []
for i in range(n):
    k = int(input())
    heapq.heappush(data, k)

result = 0
while len(data) > 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    value = a+b
    result += value
    heapq.heappush(data, value)

print(result)